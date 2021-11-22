import json

from app import db
from app.storeman.apis import post_new_product, upload_image, find_attrs_unlimitCate, find_values_attrIdUnlimit
from app.storeman.models.product_transfered import ProductTransfered

from app.storeman.stores.hd.models.brand import Brand
from app.storeman.stores.hd.models.hdproduct import HDProduct
from app.storeman.stores.hd.models.product_img import HDProductImg
from app.storeman.stores.hd.models.product_html import HDProductHtml
from app.storeman.stores.hd.models.product_item import HDProductItem
from app.storeman.stores.hd.models.product_price import HDProductPrice
from jd.api.rest.ImageWriteUpdateRequest import ImageWriteUpdateRequest

from jd.service.jd_service import save_new_product_ware, save_new_product_sku, save_new_product_img
from jd.models.product_ware import JDProductWare

from config import exchange_rate_cny
import urllib
import base64

def convert_ware_location(hd_location):
    jd_location = 1000
    if '0082' == hd_location:
        jd_location = 1000
    elif '0086' == hd_location:
        jd_location = 8
    elif '0084' == hd_location:
        jd_location = 27
    elif '0090' == hd_location:
        jd_location = 20

    return jd_location


def transfer_hd_to_jd(prd_list):
    oneprd = prd_list
    # for oneprd in prd_list:
    hd_prd = HDProduct.query.filter_by(slitmCd=oneprd).first()
    if not hd_prd:
        response_object = {
            'status': 'fail',
            'message': 'Product not exists.',
        }
        return response_object, 409

    prd = ProductTransfered.query.filter_by(product_id=oneprd, tgt_id='jd').first()
    if prd:
        response_object = {
            'status': 'fail',
            'message': 'Product already transfered.',
        }
        return response_object, 409

    """ get imgaes from hd """
    hd_prd_img = HDProductImg.query.filter_by(slitmCd=oneprd).first()
    """ get prices from hd """
    hd_prd_price = HDProductPrice.query.filter_by(slitmCd=oneprd).first()

    jd_product_ware = {
        "title": "Francoferaro 100 cowhide belt AAQV304 black", # hd_prd.slitmNm,
        "venderId": 15377431,
        # "categoryId": 1376,
        "categoryId": 12127,
        # "multiCategoryId": 1376,
        "brandId": 50382,
        # "templateId": 0,
        # "transportId": 2391212,
        "wareStatus": 1,
        "outerId": hd_prd.slitmCd,
        "itemNum": "AP-BAWTM02",
        # "barCode": "",
        # "wareLocation": convert_ware_location(hd_prd.octyCnryGbcd),
        # "delivery": 0,
        # "promiseId": 0,
        "wrap": "",
        # "packListing": "",
        "length": 50,
        "width": 10,
        "height": 100,
        "weight": 70,
        "mobileDesc": "<img src='//img13.360buyimg.com/cms/jfs/t1/214840/25/2119/478244/617a3ab9E7745b333/00af11f583017bcb.jpg' title='' alt=''>",
        "introduction": "<img src='//img13.360buyimg.com/cms/jfs/t1/214840/25/2119/478244/617a3ab9E7745b333/00af11f583017bcb.jpg' title='' alt=''>",
        # "afterSales": "",
        # "jdPrice": hd_prd_price.sellPrc * 0.9 // exchange_rate_cny if hd_prd_price else 0,
        # "marketPrice": (hd_prd_price.sellPrc // exchange_rate_cny) if hd_prd_price else 0,
        "jdPrice": 5310,
        "marketPrice": 5900,
        # "zhuangBaId": "",
        # "introductionUseFlag": "1",
        # "mobileZhuangBaId": "",
        "mobileDescUseFlag": "0",
        # "designConcept": "",
        # "fitCaseHtmlApp": "",
        # "fitCaseHtmlPc": "<html><img src='http://file1.partnerbk.com/data/savePhoto/202003/69736316910486611025.jpg' /></html>",
        # "props": ""
    }
    hd_img_fields = ['sImgNm']
    jd_product_imgs = []
    # hd_prd_img = 'http://127.0.0.1:5500/login/asdf.jpg'
    # for i in range(0, len(hd_img_fields)):
    #     """ get image from hd """
    #     # img_url = getattr(hd_prd_img, hd_img_fields[i]) if hd_prd_img else ''
    #     img_url = "https://cdn.louisclub.com/static/product/common/LLBL1AH02MH0BL0010.jpg"
    #     result = upload_image(hd_prd.slitmCd + "_" + hd_img_fields[i], img_url)
    #     jd_prd_img = {
    #         "@type": "com.jd.pop.ware.ic.api.domain.Image",
    #         "outerId": hd_prd.slitmCd,
    #         "colorId": "0000000000",
    #         "imgIndex": 1,
    #         "imgUrl": result[0]["pic_url"],
    #         # "type": "com.jd.pop.ware.ic.api.domain.Image"
    #     }
    #     print("gg")
    #     print(jd_prd_img)
    #     print("gg")
        # jd_prd_img = {
        #        "imgUrl":"jfs/t1/185285/40/18956/50810/61162570E24b2ed36/047ab30713e4daf1.jpg",
        #        "imgIndex":2,
        #        "imgId":166361614502,
        #        "colorId":"0000000000"
        # }
        # jd_product_imgs.append(jd_prd_img)
    jd_prd_img = [
        {
                    "@type": "com.jd.pop.ware.ic.api.domain.Image",
                    "outerId": "2012133095",
                    "colorId": "0000000000",
                    "imgIndex": 1,
                    "imgUrl": "jfs/t1/164631/25/26946/45856/617a31dfEa31d9535/a8eb3293417d557c.jpg",
                    # "type": "com.jd.pop.ware.ic.api.domain.Image"
                },
                {
                    "@type": "com.jd.pop.ware.ic.api.domain.Image",
                    "outerId": "2012133095",
                    "colorId": "0000000000",
                    "imgIndex": 2,
                    "imgUrl": "jfs/t1/164631/25/26946/45856/617a31dfEa31d9535/a8eb3293417d557c.jpg",
                    # "type": "com.jd.pop.ware.ic.api.domain.Image"
                },
                {
                    "@type": "com.jd.pop.ware.ic.api.domain.Image",
                    "outerId": "2012133095",
                    "colorId": "0000000000",
                    "imgIndex": 3,
                    "imgUrl": "jfs/t1/164631/25/26946/45856/617a31dfEa31d9535/a8eb3293417d557c.jpg",
                    # "type": "com.jd.pop.ware.ic.api.domain.Image"
                },
                {
                    "@type": "com.jd.pop.ware.ic.api.domain.Image",
                    "outerId": "2012133095",
                    "colorId": "0000000000",
                    "imgIndex": 4,
                    "imgUrl": "jfs/t1/164631/25/26946/45856/617a31dfEa31d9535/a8eb3293417d557c.jpg",
                    # "type": "com.jd.pop.ware.ic.api.domain.Image"
                },
                {
                    "@type": "com.jd.pop.ware.ic.api.domain.Image",
                    "outerId": "2012133095",
                    "colorId": "0000000000",
                    "imgIndex": 5,
                    "imgUrl": "jfs/t1/164631/25/26946/45856/617a31dfEa31d9535/a8eb3293417d557c.jpg",
                    # "type": "com.jd.pop.ware.ic.api.domain.Image"
                },
                {
                    "@type": "com.jd.pop.ware.ic.api.domain.Image",
                    "outerId": "2012133095",
                    "colorId": "0000000000",
                    "imgIndex": 6,
                    "imgUrl": "jfs/t1/164631/25/26946/45856/617a31dfEa31d9535/a8eb3293417d557c.jpg",
                    # "type": "com.jd.pop.ware.ic.api.domain.Image"
                }]

    # jd_product_imgs["images"] = jd_prd_img
    jd_product_ware["images"] = jd_prd_img
    # save_new_product_img(jd_product_imgs)
    # save_new_product_ware(jd_product_ware)

    saleAttrs = []
    # attrs = find_attr_UnlimitCate(jd_product_ware["multiCategoryId"], 4)
    # if "success" == attrs[0]["status"]:
    #     for saleAttr in attrs[0]["attrs"]:
    #         attrvalues = find_attr_values(saleAttr["categoryAttrId"])
    #         if attrvalues:
    #             s_attrvalues = []
    #             for attrvalue in attrvalues[0]["attrvalues"]:
    #                 s_attrvalues.append(attrvalue["id"])
    #         saleAttrs.append({
    #             # "attrValueAlias": [],
    #             "attrid": saleAttr["id"],
    #             "attrValues": s_attrvalues
    #         })

    # attrs = find_attrs_unlimitCate(jd_product_ware["categoryId"], 3)
    # if "success" == attrs[0]["status"]:
    #     for propAttr in attrs[0]["attrs"]:
    #         if propAttr["isRequired"]:
    propAttrs = [{
                    "attrId":"187521",
                    "attrValues":[
                        "933838"
                    ]
                }
            ]
            # attrvalues = fi.nd_values_attrIdUnlimit(propAttr["catId"])
            # if attrvalues:
            #     s_attrvalues = []
            #     for attrvalue in attrvalues[0]["attrvalues"]:
            #         s_attrvalues.append(str(attrvalue["id"]))
            #         break
            # propAttrs.append({
            #     # "attrValueAlias": [],
            #     "attrid": str(propAttr["id"]),
            #     "attrValues": s_attrvalues
            # })
    # jd_product_ware["multiCateProps"] = propAttrs
    jd_product_ware["props"] = propAttrs
    """ save new jd product sku """
    jd_product_sku = {
        "@type": "com.jd.pop.ware.ic.api.domain.Sku",
        # "jdPrice": hd_prd_price.sellPrc * 0.9 // exchange_rate_cny if hd_prd_price else 0,
        "jdPrice": 5310,
        "outerId": hd_prd.slitmCd,
        # "saleAttr": saleAttrs,
        "stockNum": 10,
        # "barCode": "",
        # "props": propAttrs,
        # "multiCateProps": propAttrs,
        # "type": "com.jd.pop.ware.ic.api.domain.sku"
    }
    save_new_product_sku(jd_product_sku)
    """ Send to JD """
    post_new_product(jd_product_ware, jd_product_sku)

# response_object = {
#     'status': 'success',
#     'message': 'Successfully Transfer HD to JD.',
#     'product': jd_product_ware
# }
# return response_object, 200