import enum

from app import db, flask_bcrypt
import datetime
from typing import Union

from app.storeman.utils.helpers import format_datetime


class EnumPrdCond(enum.Enum):
    New = 'N'
    Ban = 'B'
    Remain = 'R'
    Used = 'U'
    Refer = 'F'
    Scratch = 'S'

class EnumTaxType(enum.Enum):
    Tax = 'A'
    TaxFree = 'B'
    ZeroTax = 'C'

class Product(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "scm_product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prd_code = db.Column(db.String(8))
    prd_name_org = db.Column(db.String(255))
    store_id = db.Column(db.String(20))
    prd_img = db.Column(db.String(255))
    short_desc = db.Column(db.TEXT)
    price_excluding_tax = db.Column(db.DECIMAL(12, 2))
    price = db.Column(db.DECIMAL(12, 2))
    retail_price = db.Column(db.DECIMAL(12, 2))
    supply_price = db.Column(db.DECIMAL(12, 2))
    prd_condition = db.Column(db.Enum(EnumPrdCond))
    tags = db.Column(db.String(200))
    tax_type = db.Column(db.Enum(EnumTaxType))
    tax_rate = db.Column(db.DECIMAL(12,2))
    prd_volume = db.Column(db.String(45))
    cat_code = db.Column(db.String(30))
    prd_desc = db.Column(db.TEXT)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'prd_code': self.prd_code,
            'prd_name_org': self.prd_name_org,
            'store_id': self.store_id,
            'prd_img': self.prd_img,
            'short_desc': self.short_desc,
            'price_excluding_tax': float(self.price_excluding_tax),
            'price': float(self.price),
            'retail_price': float(self.retail_price),
            'supply_price': float(self.supply_price),
            'prd_condition': self.prd_condition.value,
            'tags': self.tags,
            'tax_type': self.tax_type.value,
            'tax_rate': float(self.tax_rate),
            'prd_volume': self.prd_volume,
            'cat_code': self.cat_code,
            'prd_desc': self.prd_desc,
            'created_at': format_datetime(self.created_at),
            'updated_at': format_datetime(self.updated_at)
        }
