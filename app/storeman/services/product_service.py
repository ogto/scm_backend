import datetime
import json
import pandas as pd

from sqlalchemy.sql import text
from app import db
from app.storeman.models import get_class_by_tablename
from app.storeman.models.product import Product
from app.storeman.models.store_relations import StoreRelations, EnumOpType
from app.storeman.stores.hd.service import hd_service as hd
from app.storeman.stores.hd.service import hd_transfer_service as hd_transfer
from jd.service import jd_service as jd
from typing import Dict, Tuple

from app.storeman.utils.encoder import AlchemyEncoder


def pull_products():
    _op = EnumOpType.PRODUCT
    src_stores = StoreRelations.query.filter_by(op=_op.value).all()
    for store_info in src_stores:
        src_table = store_info.src_table
        c_src_product = get_class_by_tablename(src_table)
        if c_src_product:
            product_key = getattr(c_src_product, store_info.src_key)
            kwargs = {'prd_code': None}
            product_set = db.session.query(product_key).outerjoin(Product, Product.prd_code == product_key)\
                .filter_by(**kwargs).all()

            if product_set:
                if 'hd' == store_info.src_id:
                    s_prdlist = ""
                    for i in range(0, len(product_set)):
                        if 0 == i:
                            s_prdlist = "'" + str(product_set[i][0]) + "'"
                        s_prdlist = s_prdlist + "," + "'" + str(product_set[i][0]) + "'"

                    sql = text("INSERT INTO scm_product "
                        "(prd_code, prd_name_org, store_id, prd_img, short_desc, price_excluding_tax, price, retail_price, supply_price, prd_condition, tags, tax_type, tax_rate, prd_volume, cat_code, prd_desc) "
                        "(SELECT scm_hd_product.slitmCd, slitmNm, 'hd', sImgNm, slitmNm, sellPrc * (1 - 10 / 100), sellPrc, sellPrc, csmPrc, 'New', '', 'Tax', 10, 0, 0, '' "
                        "FROM scm_hd_product inner join scm_hd_product_price on scm_hd_product.slitmCd = scm_hd_product_price.slitmCd "
                        "inner join scm_hd_product_img on scm_hd_product.slitmCd = scm_hd_product_img.slitmCd "
                        "WHERE scm_hd_product.slitmCd in ( {prdlist} )) ".format(prdlist=s_prdlist))


                    db.session.execute(sql)
                    db.session.commit()

                print(s_prdlist)

    response_object = {
        'status': 'success',
        'message': 'Product pulled successfully',
    }
    return response_object, 200



def save_new_product(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    product = Product.query.filter_by(prd_code=data['prd_code']).first()
    if not product:
        new_product = Product(
            prd_code=data['prd_code'],
            prd_name_org=data['prd_name_org'],
            store_id=data['store_id'],
            short_desc=data['short_desc'],
            price_excluding_tax=float(data['price_excluding_tax']),
            price=float(data['price']),
            retail_price=float(data['retail_price']),
            supply_price=float(data['supply_price']),
            prd_condition=data['prd_condition'],
            tags=data['tags'],
            tax_type=data['tax_type'],
            tax_rate=float(data['tax_rate']),
            prd_volume=data['prd_volume'],
            cat_code=data['cat_code'],
            prd_desc=data['prd_desc'],
            created_at=datetime.datetime.utcnow()
        )
        save_changes(new_product)

        response_object = {
            'status': 'success',
            'message': 'Product created successfully',
            'product': new_product
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product already exists.',
        }
        return response_object, 200

def save_changes(data: any) -> None:
    db.session.add(data)
    db.session.commit()


def get_all_products():
    data = Product.query.all()
    if data:
        return json.loads(json.dumps([row.serialize for row in data], cls=AlchemyEncoder))
    else:
        return []


def get_stores_products(store_id):
    data = Product.query.filter_by(store_id=store_id).all()
    if data:
        return json.loads(json.dumps([row.serialize for row in data], cls=AlchemyEncoder))
    else:
        return []


def get_a_product(product_id):
    data = Product.query.filter_by(product_id=product_id).first()
    if data:
        return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))
    else:
        return {}


def update_products_stock(store_id):
    ret_obj = None
    if 'hd' == store_id:
        ret_obj = hd.update_products_stock(store_id)

    if not ret_obj:
        response_object = {
            'status': 'fail',
            'message': 'Failed to update stock Qty. Please Log in.',
        }
        return response_object, 200
    else:
        return ret_obj


def transfer_product(src, tgt, prd_list):
    # src_table = StoreRelations.query.filter_by(op=EnumOpType.PRODUCT, src_id=src, tgt_id=tgt).all()
    # c_src_product = get_class_by_tablename(src_table)
    # src_data = Product.query.filter_by()
    ret_obj = None
    if 'hd' == src and 'jd' == tgt:
        ret_obj = hd_transfer.transfer_hd_to_jd(prd_list)
    if not ret_obj:
        response_object = {
            'status': 'fail',
            'message': 'Failed to transfer product.', 
        }
        return response_object, 200
    else:
        return ret_obj


def start_sales(store_id, product_id):
    return


def stop_sales(store_id, product_id):
    return


def product_detail(product_id):
    return


def product_detail_update(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    response_object = {
        'status': 'fail',
        'message': 'Product already exists.',
    }
    return response_object, 200

def get_store_products(store_id):
    if 'hd' == store_id:
        return hd.get_all_products()
