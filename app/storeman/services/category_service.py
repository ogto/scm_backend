import datetime
import json

from sqlalchemy.sql import text
from app import db
from app.storeman.models.category import Category
from app.storeman.stores.hd.models.category import Category as HDCategory
from jd.models.category import Category as JDCategory
from typing import Dict, Tuple

from app.storeman.utils.encoder import AlchemyEncoder


def get_all_categories():
    data = Category.query.filter_by(category_depth=3).order_by(Category.display_order).all()
    return json.loads(json.dumps(data, cls=AlchemyEncoder))


def get_store_categories(store_id):
    if "jd" == store_id:
        data = JDCategory.query.filter_by(lev=3, cat_status=1).order_by(JDCategory.indexId).all()
    elif "hd" == store_id:
        data = HDCategory.query.filter_by(lvl=3, useYn='Y').order_by(HDCategory.itemCsfCd).all()

    return json.loads(json.dumps(data, cls=AlchemyEncoder))

