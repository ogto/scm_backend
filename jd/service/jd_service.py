import json

from app import db
from jd.models.brands import JDBrands
from jd.models.category import Category
from jd.models.product_ware import JDProductWare
from jd.models.product_sku import JDProductSku
from jd.models.product_img import JDProductImg
from app.storeman.utils.encoder import AlchemyEncoder

def save_new_product_ware(data):
    prd = JDProductWare.query.filter_by(outerId=data['outerId']).first()
    if not prd:
        new_prod_ware = JDProductWare(
            title=data['title'],
            categoryId=data['categoryId'],
            # multiCategoryId=data['multiCategoryId'],
            brandId=data['brandId'],
            templateId=data['templateId'],
            transportId=data['transportId'],
            wareStatus=data['wareStatus'],
            outerId=data['outerId'],
            itemNum=data['itemNum'],
            barCode=data['barCode'],
            wareLocation=data['wareLocation'],
            delivery=data['delivery'],
            promiseId=data['promiseId'],
            wrap=data['wrap'],
            packListing=data['packListing'],
            length=data['length'],
            width=data['width'],
            height=data['height'],
            weight=data['weight'],
            mobileDesc=data['mobileDesc'],
            introduction=data['introduction'],
            afterSales=data['afterSales'],
            jdPrice=data['jdPrice'],
            marketPrice=data['marketPrice'],
            zhuangBaId=data['zhuangBaId'],
            introductionUseFlag=data['introductionUseFlag'],
            mobileZhuangBaId=data['mobileZhuangBaId'],
            mobileDescUseFlag=data['mobileDescUseFlag'],
            designConcept=data['designConcept'],
            fitCaseHtmlApp=data['fitCaseHtmlApp'],
            fitCaseHtmlPc=data['fitCaseHtmlPc']
        )
        save_changes(new_prod_ware)

        response_object = {
            'status': 'success',
            'message': 'Successfully insert Product.',
            'product': new_prod_ware
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product already exists. Please Log in.',
        }
        return response_object, 409

def save_new_product_sku(data):
    prd = JDProductSku.query.filter_by(outerId=data['outerId']).first()
    if not prd:
        new_prod_sku = JDProductSku(
            jdPrice=data['jdPrice'],
            outerId=data['outerId'],
            stockNum=data['stockNum'],
            # barCode=data['barCode'],
        )
        save_changes(new_prod_sku)
        response_object = {
            'status': 'success',
            'message': 'Successfully insert Hyundai Product HTML.',
            'product': new_prod_sku
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_new_product_img(datas):
    imgidx = 0
    new_prd_imgs = []
    for data in datas:
        prd = JDProductImg.query.filter_by(outerId=data['outerId'], imgIndex=imgidx).first()
        if not prd:
            new_prod_img = JDProductImg(
                outerId=data['outerId'],
                colorId='0000000000',
                imgIndex=imgidx,
                imgUrl=data['imgUrl'],
            )
            new_prd_imgs.append(new_prod_img)

            try:
                save_changes(new_prod_img)
                imgidx = imgidx + 1
            except:
                response_object = {
                    'status': 'fail',
                    'message': 'SKU already exists. Please Log in.',
                }
                return response_object, 409

    response_object = {
        'status': 'success',
        'message': 'Successfully insert Product SKU.',
        'product': new_prd_imgs
    }
    return response_object, 200


def save_new_brand(data):
    for brand in data:
        brd = JDBrands.query.filter_by(erpBrandId=brand['erpBrandId']).first()
        if not brd:
            new_brand = JDBrands(
                erpBrandId=brand["erpBrandId"],
                brandName=brand["brandName"]
            )
            save_changes(new_brand)
        # else:
        #     response_object = {
        #         'status': 'fail',
        #         'message': 'Error occured during saving new brand code',
        #     }
        #     return response_object, 409

    response_object = {
        'status': 'success',
        'message': 'Successfully insert JD Brands.',
        'product': data
    }
    return response_object, 200

def save_new_category(data):
    for cate in data:
        cat = Category.query.filter_by(id=cate["id"]).first()
        if not cat:
            new_cate = Category(
                id=cate["id"],
                fid=cate["fid"],
                indexId=cate["indexId"],
                cat_name=cate["name"],
                aliasName=cate["aliasName"],
                cat_status=cate["status"],
                lev=cate["lev"],
            )
            save_changes(new_cate)
        # else:
        #     response_object = {
        #         'status': 'fail',
        #         'message': 'Error occured during saving new brand code',
        #     }
        #     return response_object, 409

    response_object = {
        'status': 'success',
        'message': 'Successfully insert JD Brands.',
        'product': data
    }
    return response_object, 200


def save_changes(data: any) -> None:
    db.session.add(data)
    db.session.commit()


def get_category():
    data = Category.query.filter_by(lev=3, cat_status=1).order_by(Category.fid, Category.indexId).all()
    return json.loads(json.dumps(data, cls=AlchemyEncoder))
