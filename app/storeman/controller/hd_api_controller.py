from flask import request, session
from flask_restx import Resource

from app.storeman.dtos.hd_dto import HDDto
from app.storeman.apis.hyundai import get_products_by_brand, get_product_detail, get_category
from app.storeman.stores.hd.service.hd_service import get_new_product_list, save_new_product_sell, get_all_products, \
    save_categories
from app.storeman.stores.hd.service.hd_service import save_new_brand_prd, save_new_product_detail, save_new_product_img, save_new_product_html, save_new_product_item, save_new_product_price
from app.storeman.services.user_service import get_user_by_id
from bs4 import BeautifulSoup

import json
import xmltodict

api = HDDto.api
_product = HDDto.product

@api.route('/category')
class HDCategory(Resource):
    @api.doc('hyundai_product_category')
    @api.param('itemCsfGbcd', '상품분류구분코드')
    @api.param('itemCsfCd', '상품분류코드')
    @api.response(201, 'List from hyundai storeman products')
    def get(self):
        """
        List all hyundai's category
        """
        user_info = get_user_by_id(session["_user_id"])
        userid = user_info.client_id
        userkey = user_info.client_key
        # userid = '004503A02152'
        # userkey = 'FF08E75795EBA14E770E713A3CFC844D'

        itemCsfGbcd = request.args.get('itemCsfGbcd')
        itemCsfCd = request.args.get('itemCsfCd')

        if not itemCsfGbcd:
            itemCsfGbcd = 40

        if not itemCsfCd:
            itemCsfCd = ''

        payload = f"""<?xml version="1.0" encoding="utf-8" ?> 
            <Root>
                <Dataset id="dsCond">
                    <rows>
                        <row>
                            <itemCsfGbcd>{itemCsfGbcd}</itemCsfGbcd> 
                            <itemCsfCd>{itemCsfCd}</itemCsfCd>  
                        </row>
                    </rows>
                </Dataset>
            </Root>"""

        xml = get_category(userid, userkey, payload)
        json_text = json.dumps(xmltodict.parse(xml.text.replace('\n', '').replace('\t', '')), indent=4)
        json_obj = json.loads(json_text)

        res2xml = json_obj.get('Response2XML')
        if res2xml:
            dataset = res2xml.get('Dataset')
            for ds in dataset:
                dsitem = ds.get('@id')

                if 'dsList' == dsitem:
                    rows = ds.get('rows')
                    for row in rows.get('row'):
                        save_categories(row)

                    response_object = {
                        'status': 'success',
                        'message': 'Category Inserted Successfully!',
                    }
                    return response_object, 200
                elif 'result' == dsitem:
                    pass
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'No category founded.',
                    }
                    return response_object, 200


@api.route('/product/detail')
class HDProductDetail(Resource):
    @api.doc('detail_of_hyundai_products')
    @api.param('brndcd', '브랜드코드')
    @api.param('slitmcd', '상품코드')
    @api.response(201, 'List from hyundai storeman products')
    def get(self):
        """
        List all hyundai's products
        """

        brndcd = request.args.get('brndcd')
        slitmcd = request.args.get('slitmcd')
        product_list = get_new_product_list(brndcd)


        userid = '004503A02152'
        userkey = 'FF08E75795EBA14E770E713A3CFC844D'
        all_parsed_dict = []
        item_parsed_dict = []
        price_parsed_dict = []
        img_parsed_dict = []
        sell_parsed_dict = []
        html_parsed_dict = []
        # if not slitmcd:
        # for prd in product_list:
        #     slitmcd = prd[0]
        payload = f"""<?xml version="1.0" encoding="utf-8" ?>
            <Root>
                <Dataset id="dsCond">
                    <rows>
                        <row>
                            <brndCd>{brndcd}</brndCd>
                            <slitmCd>{slitmcd}</slitmCd>
                        </row>
                    </rows>
                </Dataset>
            </Root>"""
        xml = get_product_detail(userid, userkey, payload)
        soup = BeautifulSoup(xml.text, "lxml") #.prettify(formatter="html")

        s = soup.find_all('dataset')
        try:
            for ds in s:
                if ds['id'] == 'dsItem':
                    parsed_dict = xmltodict.parse(str(ds))
                    all_parsed_dict.append(parsed_dict)
                elif ds['id'] == 'dsItemCsfCd':
                    parsed_dict = xmltodict.parse(str(ds))
                    item_parsed_dict.append(parsed_dict)
                elif ds['id'] == 'dsSlitmPrcAthzHis':
                    parsed_dict = xmltodict.parse(str(ds))
                    price_parsed_dict.append(parsed_dict)
                elif ds['id'] == 'dsItemImgDtl':
                    parsed_dict = xmltodict.parse(str(ds))
                    img_parsed_dict.append(parsed_dict)
                elif ds['id'] == 'dsHtmlItstMst':
                    parsed_dict = xmltodict.parse(str(ds))
                    html_parsed_dict.append(parsed_dict)
                elif ds['id'] == 'dsSellUitmDtl':
                    parsed_dict = xmltodict.parse(str(ds))
                    sell_parsed_dict.append(parsed_dict)

        except:
            response_object = {
                'status': 'fail',
                'message': 'No product found.',
            }
            return response_object, 200

        for json_obj in all_parsed_dict:
            json_ds = json_obj.get('dataset')
            if 'dsItem' == json_ds['@id']:
                rows = json_ds.get('rows')
                if rows:
                    _row = rows.get('row')
                    if isinstance(_row, list):
                        for row in _row:
                            save_new_product_detail(row)
                    else:
                        save_new_product_detail(_row)

        for json_obj in item_parsed_dict:
            json_ds = json_obj.get('dataset')
            if 'dsItemCsfCd' == json_ds['@id']:
                rows = json_ds.get('rows')
                if rows:
                    _row = rows.get('row')
                    if isinstance(_row, list):
                        for row in _row:
                            save_new_product_item(slitmcd, row)
                    else:
                        save_new_product_item(slitmcd, _row)


        for json_obj in price_parsed_dict:
            json_ds = json_obj.get('dataset')
            if 'dsSlitmPrcAthzHis' == json_ds['@id']:
                rows = json_ds.get('rows')
                if rows:
                    _row = rows.get('row')
                    if isinstance(_row, list):
                        for row in _row:
                            save_new_product_price(row)
                    else:
                        save_new_product_price(_row)

        for json_obj in img_parsed_dict:
            json_ds = json_obj.get('dataset')
            if 'dsItemImgDtl' == json_ds['@id']:
                rows = json_ds.get('rows')
                if rows:
                    _row = rows.get('row')
                    if isinstance(_row, list):
                        for row in _row:
                            save_new_product_img(row)
                    else:
                        save_new_product_img(_row)

        for json_obj in sell_parsed_dict:
            json_ds = json_obj.get('dataset')
            if 'dsSellUitmDtl' == json_ds['@id']:
                rows = json_ds.get('rows')
                if rows:
                    _row = rows.get('row')
                    if isinstance(_row, list):
                        for row in _row:
                            save_new_product_sell(row)
                    else:
                        save_new_product_sell(_row)

        for json_obj in html_parsed_dict:
            json_ds = json_obj.get('dataset')
            if 'dsHtmlItstMst' == json_ds['@id']:
                rows = json_ds.get('rows')
                if rows:
                    _row = rows.get('row')
                    if isinstance(_row, list):
                        for row in _row:
                            save_new_product_html(row)
                    else:
                        save_new_product_html(_row)

        # all_parsed_dict = []
        # item_parsed_dict = []
        # price_parsed_dict = []
        # img_parsed_dict = []
        # html_parsed_dict = []


        response_object = {
            'status': 'success',
            'message': 'hyundai products details inserted successfully.',
            'products': all_parsed_dict
        }
        return response_object, 200


@api.route('/product/detailall')
class HDProductDetailAll(Resource):
    @api.doc('detail_of_all_hyundai_products')
    @api.param('brndcd', '브랜드코드')
    @api.response(201, 'List from all hyundai storeman products')
    def get(self):
        """
        List all hyundai's products
        """

        brndcd = request.args.get('brndcd')
        product_list = get_new_product_list(brndcd)

        userid = '004503A02152'
        userkey = 'FF08E75795EBA14E770E713A3CFC844D'
        all_parsed_dict = []
        item_parsed_dict = []
        price_parsed_dict = []
        img_parsed_dict = []
        sell_parsed_dict = []
        html_parsed_dict = []

        for prd in product_list:
            slitmcd = prd[0]
            payload = f"""<?xml version="1.0" encoding="utf-8" ?>
                <Root>
                    <Dataset id="dsCond">
                        <rows>
                            <row>
                                <brndCd>{brndcd}</brndCd>
                                <slitmCd>{slitmcd}</slitmCd>
                            </row>
                        </rows>
                    </Dataset>
                </Root>"""
            xml = get_product_detail(userid, userkey, payload)
            soup = BeautifulSoup(xml.text, "lxml") #.prettify(formatter="html")

            s = soup.find_all('dataset')
            try:
                for ds in s:
                    if ds['id'] == 'dsItem':
                        parsed_dict = xmltodict.parse(str(ds))
                        all_parsed_dict.append(parsed_dict)
                    elif ds['id'] == 'dsItemCsfCd':
                        parsed_dict = xmltodict.parse(str(ds))
                        item_parsed_dict.append(parsed_dict)
                    elif ds['id'] == 'dsSlitmPrcAthzHis':
                        parsed_dict = xmltodict.parse(str(ds))
                        price_parsed_dict.append(parsed_dict)
                    elif ds['id'] == 'dsItemImgDtl':
                        parsed_dict = xmltodict.parse(str(ds))
                        img_parsed_dict.append(parsed_dict)
                    elif ds['id'] == 'dsHtmlItstMst':
                        parsed_dict = xmltodict.parse(str(ds))
                        html_parsed_dict.append(parsed_dict)
                    elif ds['id'] == 'dsSellUitmDtl':
                        parsed_dict = xmltodict.parse(str(ds))
                        sell_parsed_dict.append(parsed_dict)

            except:
                response_object = {
                    'status': 'fail',
                    'message': 'No product found.',
                }
                return response_object, 200

            for json_obj in all_parsed_dict:
                json_ds = json_obj.get('dataset')
                if 'dsItem' == json_ds['@id']:
                    rows = json_ds.get('rows')
                    if rows:
                        _row = rows.get('row')
                        if isinstance(_row, list):
                            for row in _row:
                                save_new_product_detail(row)
                        else:
                            save_new_product_detail(_row)

            for json_obj in item_parsed_dict:
                json_ds = json_obj.get('dataset')
                if 'dsItemCsfCd' == json_ds['@id']:
                    rows = json_ds.get('rows')
                    if rows:
                        _row = rows.get('row')
                        if isinstance(_row, list):
                            for row in _row:
                                save_new_product_item(slitmcd, row)
                        else:
                            save_new_product_item(slitmcd, _row)


            for json_obj in price_parsed_dict:
                json_ds = json_obj.get('dataset')
                if 'dsSlitmPrcAthzHis' == json_ds['@id']:
                    rows = json_ds.get('rows')
                    if rows:
                        _row = rows.get('row')
                        if isinstance(_row, list):
                            for row in _row:
                                save_new_product_price(row)
                        else:
                            save_new_product_price(_row)

            for json_obj in img_parsed_dict:
                json_ds = json_obj.get('dataset')
                if 'dsItemImgDtl' == json_ds['@id']:
                    rows = json_ds.get('rows')
                    if rows:
                        _row = rows.get('row')
                        if isinstance(_row, list):
                            for row in _row:
                                save_new_product_img(row)
                        else:
                            save_new_product_img(_row)

            for json_obj in sell_parsed_dict:
                json_ds = json_obj.get('dataset')
                if 'dsSellUitmDtl' == json_ds['@id']:
                    rows = json_ds.get('rows')
                    if rows:
                        _row = rows.get('row')
                        if isinstance(_row, list):
                            for row in _row:
                                save_new_product_sell(row)
                        else:
                            save_new_product_sell(_row)

            for json_obj in html_parsed_dict:
                json_ds = json_obj.get('dataset')
                if 'dsHtmlItstMst' == json_ds['@id']:
                    rows = json_ds.get('rows')
                    if rows:
                        _row = rows.get('row')
                        if isinstance(_row, list):
                            for row in _row:
                                save_new_product_html(row)
                        else:
                            save_new_product_html(_row)

            all_parsed_dict = []
            item_parsed_dict = []
            price_parsed_dict = []
            img_parsed_dict = []
            html_parsed_dict = []
            sell_parsed_dict = []


        response_object = {
            'status': 'success',
            'message': 'hyundai products details inserted successfully.',
            'products': all_parsed_dict
        }
        return response_object, 200


@api.route('/brands')
class HDBrand(Resource):
    @api.doc('list_of_hyundai_products')
    @api.param('brndcd', '브랜드 코드')
    # @admin_token_required
    @api.response(201, 'List from hyundai storeman products')
    def get(self):
        """
        List all hyundai's products
        """
        brndcd = request.args.get('brndcd')

        userid = '004503A02152'
        userkey = 'FF08E75795EBA14E770E713A3CFC844D'
        payload = f"""<?xml version="1.0" encoding="utf-8" ?>
            <Root>
                <Dataset id="dsCond">
                    <rows>
                        <row>
                            <brndCd>{brndcd}</brndCd>
                        </row>
                    </rows>
                </Dataset>
            </Root>"""
        xml = get_products_by_brand(userid, userkey, payload)
        json_text = json.dumps(xmltodict.parse(xml.text.replace('\n', '').replace('\t', '')), indent=4)
        json_obj = json.loads(json_text)

        res2xml = json_obj.get('Response2XML')
        if res2xml:
            dataset = res2xml.get('Dataset')
            for ds in dataset:
                dsitem = ds.get('@id')

                if 'dsItem' == dsitem:
                    rows = ds.get('rows')
                    for row in rows.get('row'):
                        save_new_brand_prd(row)

                    response_object = {
                        'status': 'success',
                        'message': 'Brand Insert Succeeded!',
                    }
                    return response_object, 200
                elif 'result' == dsitem:
                    pass
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'No product found.',
                    }
                    return response_object, 200

@api.route('/brandslist')
class HDBrand(Resource):
    @api.doc('get_hyundai_brand_list')
    @api.param('brndcd', '브랜드 코드')
    # @admin_token_required
    @api.response(201, 'List from hyundai storeman products')
    def get(self):
        """
        List all hyundai's products
        """
        brndcds = request.args.get('brndcd')

        userid = '004503A02152'
        userkey = 'FF08E75795EBA14E770E713A3CFC844D'

        for brndcd in brndcds:
            payload = f"""<?xml version="1.0" encoding="utf-8" ?>
                <Root>
                    <Dataset id="dsCond">
                        <rows>
                            <row>
                                <brndCd>{brndcd}</brndCd>
                            </row>
                        </rows>
                    </Dataset>
                </Root>"""
            xml = get_products_by_brand(userid, userkey, payload)
            json_text = json.dumps(xmltodict.parse(xml.text.replace('\n', '').replace('\t', '')), indent=4)
            json_obj = json.loads(json_text)

            res2xml = json_obj.get('Response2XML')
            if res2xml:
                dataset = res2xml.get('Dataset')
                for ds in dataset:
                    dsitem = ds.get('@id')

                    if 'dsItem' == dsitem:
                        rows = ds.get('rows')
                        for row in rows.get('row'):
                            save_new_brand_prd(row)
                    elif 'result' == dsitem:
                        pass
                    else:
                        response_object = {
                            'status': 'fail',
                            'message': 'No product found.',
                        }
                        return response_object, 200
                    
        response_object = {
            'status': 'success',
            'message': 'Brand Insert Succeeded!',
        }
        return response_object, 200

@api.route('/products')
class HDProductList(Resource):
    @api.doc('hd product detail')
    @api.response(201, 'hyundai product list')
    def get(self):
        """
        Hyundai's product list
        """
        return get_all_products()



@api.route('/product/<product_id>')
@api.param('product_id', 'The Product identifier')
@api.response(404, 'Product not found.')
class HDProduct(Resource):
    @api.doc('jingdong_products detail')
    # @admin_token_required
    @api.response(201, 'jingdong products detail')
    def get(self, product_id):
        """
        Hyundai's products detail
        """
        store_id = request.args.get("store_id")
        return get_product_detail(store_id, product_id)

    @api.doc('post_new_product')
    # @admin_token_required
    @api.response(201, 'product registered successfully')
    def post(self):
        """
        List all jd's products
        """
        post_new_product()

    @api.doc('update_product_detail')
    # @admin_token_required
    @api.response(201, 'product updated successfully')
    def put(self):
        """
        Update product
        """
        update_product()

    @api.doc('delete_a_product')
    # @admin_token_required
    @api.response(201, 'product deleted successfully')
    def delete(self):
        """
        delete a product
        """
        delete_product()
