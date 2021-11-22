import enum

from app import db, flask_bcrypt

class EnumOpType(enum.Enum):
    PRODUCT = 'PRODUCT'
    ORDER = 'ORDER'

class StoreRelations(db.Model):
    """ Store Relation Model for storing store related details """
    __tablename__ = "scm_store_relations"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    op = db.Column(db.Enum(EnumOpType), default=EnumOpType.PRODUCT.value)
    src_id = db.Column(db.String(10))
    tgt_id = db.Column(db.String(10))
    src_table = db.Column(db.String(100))
    tgt_table = db.Column(db.String(100))
    src_key = db.Column(db.String(100))
    tgt_key = db.Column(db.String(100))
    created_at = db.Column(db.DATETIME)

class StoreFields(db.Model):
    """ Store Relation Model for storing store related details """
    __tablename__ = "scm_store_fields"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    relation_id = db.Column(db.BigInteger)
    seq = db.Column(db.Integer)
    src_field = db.Column(db.String(100))
    tgt_field = db.Column(db.String(100))

