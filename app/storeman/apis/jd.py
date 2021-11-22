import base64
import io
import json
import urllib

import jd
from jd.api.rest.CategoryReadFindAttrByIdUnlimitCateRequest import \
    CategoryReadFindAttrByIdUnlimitCateRequest
from jd.api.rest.CategoryReadFindAttrsByCategoryIdRequest import \
    CategoryReadFindAttrsByCategoryIdRequest
from jd.api.rest.ImageWriteUpdateRequest import ImageWriteUpdateRequest
from jd.api.rest.ImgzonePictureUploadRequest import ImgzonePictureUploadRequest
from jd.api.rest.PopOrderSearchRequest import PopOrderSearchRequest
from jd.config import Config
from jd.models.brands import JDBrands
from jd.security.tde.tde_exceptions import ServiceErrorException
from jd.api.rest.WareWriteAddRequest import WareWriteAddRequest, Ware, Sku
from jd.api.rest.WareWriteUpdateWareRequest import WareWriteUpdateWareRequest
from jd.api.rest.WareWriteDeleteRequest import WareWriteDeleteRequest
from jd.api.rest.PopOrderGetRequest import PopOrderGetRequest
from jd.api.rest.PopOrderEnSearchRequest import PopOrderEnSearchRequest
from jd.api.rest.SkuReadFindSkuByIdRequest import SkuReadFindSkuByIdRequest
from jd.api.rest.SkuReadSearchSkuListRequest import SkuReadSearchSkuListRequest
from jd.api.rest.ImageReadFindImagesByWareIdRequest import ImageReadFindImagesByWareIdRequest
from jd.api.rest.WareReadSearchWare4ValidRequest import WareReadSearchWare4ValidRequest
from jd.api.rest.PopVenderCenerVenderBrandQueryRequest import PopVenderCenerVenderBrandQueryRequest
from jd.api.rest.VenderCategoryGetFullValidCategoryResultByVenderIdRequest import \
    VenderCategoryGetFullValidCategoryResultByVenderIdRequest
from jd.service.jd_service import save_new_brand, save_new_category
from jd.api.rest.SkuFareTemplateServiceGetTemplatesRequest import SkuFareTemplateServiceGetTemplatesRequest
from jd.api.rest.CategoryReadFindAttrsByCategoryIdUnlimitCateRequest import CategoryReadFindAttrsByCategoryIdUnlimitCateRequest
from jd.api.rest.CategoryReadFindValuesByAttrIdUnlimitRequest import CategoryReadFindValuesByAttrIdUnlimitRequest
from jd.api.rest.WareReadFindWareByIdRequest import WareReadFindWareByIdRequest


def jd_store_init():
    # only need to init one time
    jd.setDefaultAppInfo(Config.CONFIG['APP_KEY'], Config.CONFIG['APP_SECRET'])
    # tcc = TdeClientCache()
    # ins = tcc.instance('storeman.jd.com', "0e52584b16724fec9a3f1a16c9e3de894ngi", "A9BD72B9A4842DC621554893C1D1D1D1", "84043e78056a485db9201e94b22e8499")


def get_sku(skuid):
    req = SkuReadFindSkuByIdRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.skuId = skuid
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    category_read_response = json_response.get('jingdong_vender_category_getFullValidCategoryResultByVenderId_responce')
    if category_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % category_read_response.get('errorMessage'))

    category = category_read_response.get('returnType').get('list')

    save_new_category(category)

    if category is None:
        response_object = {
            'status': 'fail',
            'message': 'No category found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'category': category
        }
        return response_object, 200


def get_sku_list(page, size):
    req = SkuReadSearchSkuListRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.page_size = size
    req.pageNo = page
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    category_read_response = json_response.get('jingdong_sku_read_searchSkuList_responce')
    if not category_read_response:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % category_read_response.get('errorMessage'))

    if "0" == category_read_response.get("code"):
        skus = category_read_response.get('page').get('data')

    # save_new_category(category)

    if skus is None:
        response_object = {
            'status': 'fail',
            'message': 'No category found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'skus': skus
        }
        return response_object, 200


def get_product_list(page=1, size=20):
    req = WareReadSearchWare4ValidRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    # req = SkuReadSearchSkuListRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    if page < 1:
        page = 1
    req.pageNo = page
    req.pageSize = size
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    product_read_response = json_response.get('jingdong_ware_read_searchWare4Valid_responce')
    # product_read_response = json_response.get('jingdong_sku_read_searchSkuList_responce')
    if '0' != product_read_response.get('code'):
        raise ServiceErrorException('gw platform error -> %s' % product_read_response.get('errorMessage'))
    page_size = product_read_response.get('pageSize')
    page_no = product_read_response.get('pageNo')
    total_cnt = product_read_response.get('totalItem')
    products = product_read_response.get('page').get('data')
    if products is None:
        response_object = {
            'status': 'fail',
            'message': 'No product found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'product list successfully',
            'products': product_read_response
        }
        return response_object, 200


def get_product():
    # req = WareReadFindWareByIdRequest()
    # req = SkuReadFindSkuByIdRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req = WareReadFindWareByIdRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.wareId = '1976854215'
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    # product_read_response = json_response.get('jingdong_ware_read_findWareById_responce')
    print("asdasdasdasdasd")
    print(json.dumps(json_response, indent=2))
    print("asdasdasdasdasd")
    product_read_response = json_response.get('jingdong_ware_read_findWareById_responce')
    if product_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % product_read_response.get('errorMessage'))
    product = product_read_response.get('ware')
    if product is None:
        response_object = {
            'status': 'fail',
            'message': 'No product found.',
        }
        return response_object, 404
    else:
        response_object = {
            'status': 'success',
            'message': 'product list successfully',
            'product': product
        }
        return response_object, 200


def get_product_images(product_id):
    # req = WareReadFindWareByIdRequest()
    req = ImageReadFindImagesByWareIdRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.wareId = product_id
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    # product_read_response = json_response.get('jingdong_ware_read_findWareById_responce')
    product_read_response = json_response.get('jingdong_image_read_findImagesByWareId_responce')
    if product_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % product_read_response.get('errorMessage'))
    product = product_read_response.get('ware')
    if product is None:
        response_object = {
            'status': 'fail',
            'message': 'No product found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'product list successfully',
            'product': product
        }
        return response_object, 200


def get_approved_brand(brandname):
    req = PopVenderCenerVenderBrandQueryRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    if brandname:
        brandname = ''
    req.name = brandname
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    brand_read_response = json_response.get('jingdong_pop_vender_cener_venderBrand_query_responce')
    if brand_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % brand_read_response.get('errorMessage'))
    brands = brand_read_response.get('brandList')

    """ save new brand """
    save_new_brand(brands)

    if brands is None:
        response_object = {
            'status': 'fail',
            'message': 'No product found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'product list successfully',
            'brands': brands
        }
        return response_object, 200

def find_attr_categoryId(cid, type):
    req = CategoryReadFindAttrsByCategoryIdRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.cid = cid
    req.attributeType = type
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    category_read_response = json_response.get('jingdong_category_read_findAttrsByCategoryId_responce')
    if category_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % category_read_response.get('errorMessage'))
    attrs = category_read_response.get('categoryAttrs')
    if attrs is None:
        response_object = {
            'status': 'fail',
            'message': 'No category found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'attrs': attrs
        }
        return response_object, 200


def find_attrs_unlimitCate(cid, type):
    req = CategoryReadFindAttrsByCategoryIdUnlimitCateRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.cid = cid
    req.attributeType = type

    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    category_read_response = json_response.get('jingdong_category_read_findAttrsByCategoryIdUnlimitCate_responce')
    if not category_read_response:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % category_read_response.get('errorMessage'))
    attrs = category_read_response.get('findattrsbycategoryidunlimitcate_result')
    if attrs is None:
        response_object = {
            'status': 'fail',
            'message': 'No Attributes found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'Get Attributes successfully',
            'attrs': attrs
        }
        return response_object, 200


def find_attr_values(cai):
    req = CategoryReadFindValuesByAttrIdUnlimitRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.categoryAttrId = cai
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    attr_read_response = json_response.get('jingdong_category_read_findValuesByAttrIdUnlimit_responce')
    if attr_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % attr_read_response.get('errorMessage'))
    attrvalues = attr_read_response.get('findvaluesbyattridunlimit_result')
    if attrvalues is None:
        response_object = {
            'status': 'fail',
            'message': 'No category found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'attrvalues': attrvalues
        }
        return response_object, 200


def find_values_attrIdUnlimit(cai):
    req = CategoryReadFindValuesByAttrIdUnlimitRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.categoryAttrId = cai
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    attr_read_response = json_response.get('jingdong_category_read_findValuesByAttrIdUnlimit_responce')
    if attr_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % attr_read_response.get('errorMessage'))
    attrvalues = attr_read_response.get('findvaluesbyattridunlimit_result')
    if attrvalues is None:
        response_object = {
            'status': 'fail',
            'message': 'No category found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'attrvalues': attrvalues
        }
        return response_object, 200


def get_transport_template_list():
    req = SkuFareTemplateServiceGetTemplatesRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    template_response = json_response.get('jingdong_SkuFareTemplateService_getTemplates_responce')

    if template_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % template_response.get('errorMessage'))

    template_list = template_response.get('query_skuFareTemplate_result').get('template_list')

    if template_list is None:
        response_object = {
            'status': 'fail',
            'message': 'No transport templates found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'templates': template_list
        }
        return response_object, 200


def get_valid_categorys():
    req = VenderCategoryGetFullValidCategoryResultByVenderIdRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    category_read_response = json_response.get('jingdong_vender_category_getFullValidCategoryResultByVenderId_responce')
    if category_read_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % category_read_response.get('errorMessage'))

    category = category_read_response.get('returnType').get('list')

    save_new_category(category)

    if category is None:
        response_object = {
            'status': 'fail',
            'message': 'No category found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'category': category
        }
        return response_object, 200


def upload_image(_name, url):
    contents = urllib.request.urlopen(url).read()
    data = base64.b64encode(contents)
    # data = io.BytesIO(contents)
    req = ImgzonePictureUploadRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    req.image_data = data
    req.picture_name = _name
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'], ssl=True)
    print("3333")
    print(json_response)
    # json.loads(json_response)
    imgzone_upload_response = json_response.get('jingdong_imgzone_picture_upload_responce')
    if not imgzone_upload_response:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error -> %s' % error_response.get('message'))

    if 1 != imgzone_upload_response.get("return_code"):
        response_object = {
            'status': 'fail',
            'message': 'No category found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'category list successfully',
            'pic_url': imgzone_upload_response.get("picture_url")
        }
        return response_object, 200


def post_new_product(wares, skus):
    # get_product()
    req = WareWriteAddRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    # temp_ware = json.dumps(wares)
    # temp_skus = json.dumps(skus)
    # wares = wares
    # skus = skus
    # req.ware = wares
    req.ware = wares
    # req.ware['skus'] = [skus]

    status = 1
    req.ware['wareStatus'] = status


    req.skus = [skus]
    # print("temp")s
    # print(temp_ware)
    # print(temp_skus)
    # print("temp")

    # ware = Ware()
    # # sk = Sku()

    # # ware.venderId = 10638702
    # ware.title = wares['title']
    # ware.categoryId = wares['categoryId']
    # # ware.multiCategoryId = wares['multiCategoryId']
    # ware.brandId = wares['brandId']
    # ware.templateId = wares['templateId']
    # ware.transportId = wares['transportId']
    # ware.wareStatus = wares['wareStatus']
    # ware.outerId = wares['outerId']
    # ware.itemNum = wares['itemNum']
    # ware.barCode = wares['barCode']
    # ware.wareLocation = wares['wareLocation']
    # ware.delivery = wares['delivery']
    # ware.promiseId = wares['promiseId']
    # # ware.adWords = None
    # ware.wrap = wares['wrap']
    # ware.packListing = wares['packListing']
    # # ware.length = wares['length']
    # # ware.width = wares['width']
    # # ware.height = wares['height']
    # # ware.weight = wares['weight']
    # ware.props = wares['props']
    # # ware.features = []

    # ware.images = wares['images']
    # # ware.images = None
    # # ware.shopCategorys = []
    # ware.mobileDesc = wares['mobileDesc']
    # ware.introduction = wares['introduction']
    # ware.afterSales = wares['afterSales']
    # ware.jdPrice = wares['jdPrice']
    # ware.marketPrice = wares['marketPrice']
    # ware.zhuangBaId = wares['zhuangBaId']
    # ware.introductionUseFlag = wares['introductionUseFlag']
    # ware.mobileZhuangBaId = wares['mobileZhuangBaId']
    # ware.mobileDescUseFlag = wares['mobileDescUseFlag']
    # ware.designConcept = wares['designConcept']
    # ware.fitCaseHtmlApp = wares['fitCaseHtmlApp']
    # ware.fitCaseHtmlPc = wares['fitCaseHtmlPc']
    # ware.specialServices = []
    # # ware.multiCateProps = wares['multiCateProps']

    # sku = Sku()
    # sku.venderId = 10638702
    # sku.jdPrice = skus['jdPrice']
    # sku.outerId = skus['outerId']
    # sku.barCode = ""
    # sku.stockNum = skus['stockNum']
    # # sku.saleAttrs = skus['saleAttr']
    # sku.features = []
    # # sku.props = skus['props']
    # # sku.multiCateProps = skus['multiCateProps']
    # sku.capacity = ''

    # req.ware = json.loads(json.dumps(ware.__dict__, ensure_ascii=False))
    # req.skus = json.loads(json.dumps(sku.__dict__, ensure_ascii=False))
    # list_sku = [json.loads(json.dumps(sku.__dict__, ensure_ascii=False))]
    # # list_sku = []
    # req.skus = list_sku
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'],ssl=True)
    print(json.dumps(json_response, ensure_ascii=False))
    print("=======================")
    try:
        product_write_response = json_response.get('jingdong_ware_write_add_responce')
        # print(product_write_response.get('ware'))

        print("asdasd")
        print(product_write_response)
        if product_write_response is None:
            error_response = json_response.get('error_response')
            if '0' != error_response.get('code'):
                raise ServiceErrorException('gw platform error -> %s' % product_write_response.get('errorMessage'))

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e,
        }
        return response_object, 409

    product = product_write_response.get('ware')
    print(product)
    if product is None:
        response_object = {
            'status': 'fail',
            'message': 'No product found.',
            'product': product
        }
        return response_object, 409
    else:
        print("이거?")
        response_object = {
            'status': 'success',
            'message': 'product list successfully',
            'product': product
        }
        return response_object, 200


def update_product():
    req = WareWriteUpdateWareRequest()
    res = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    print(json.dumps(res, ensure_ascii=False))


def delete_product():
    req = WareWriteDeleteRequest()
    res = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    print(json.dumps(res, ensure_ascii=False))


def get_order_list():
    req = PopOrderSearchRequest('api.jd.com', 80)
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    print(json_response)
    order_search_response = json_response.get('jingdong_pop_order_search_responce')

    if not order_search_response:
        error_response = json_response.get('error_response')
        print(error_response)
        response_object = {
            'status': 'fail',
            'message': error_response.get('en_desc'),
        }
        return response_object, 409

    # if 'true' != order_search_response.get('searchorderinfo_result').get('apiResult').get('success'):
    #     raise ServiceErrorException('gw platform error -> %s' % order_search_response.get('numberCode'))

    order_info_list = order_search_response.get('orderInfoList')
    # page_size = order_search_response.get('pageSize')
    # page_no = order_search_response.get('pageNo')
    # total_cnt = order_search_response.get('totalItem')
    # products = order_search_response.get('page').get('data')
    if order_info_list is None:
        response_object = {
            'status': 'fail',
            'message': 'No order found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'order list successfully',
            'order': order_info_list
        }
        return response_object, 200


def get_order(order_id):
    req = PopOrderGetRequest()
    req.order_id = order_id
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    order_get_response = json_response.get('jingdong_pop_order_get_response')
    if order_get_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error code -> %s' % error_response.get('zh_desc'))

    order = order_get_response.get('orderDetailInfo').get('orderInfo')
    if order is None:
        response_object = {
            'status': 'fail',
            'message': 'No order found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'get order successfully',
            'order': order
        }
        return response_object, 200

def get_vender_brand():
    req = PopVenderCenerVenderBrandQueryRequest(Config.CONFIG['DOMAIN'], Config.CONFIG['PORT'])
    json_response = req.getResponse(Config.CONFIG['ACCESS_TOKEN'])
    order_get_response = json_response.get('jingdong_pop_order_get_response')
    if order_get_response is None:
        error_response = json_response.get('error_response')
        if '0' != error_response.get('code'):
            raise ServiceErrorException('gw platform error code -> %s' % error_response.get('zh_desc'))

    order = order_get_response.get('orderDetailInfo').get('orderInfo')
    if order is None:
        response_object = {
            'status': 'fail',
            'message': 'No order found.',
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'get order successfully',
            'order': order
        }
        return response_object, 200

if __name__ == '__main__':
    jd_store_init()
