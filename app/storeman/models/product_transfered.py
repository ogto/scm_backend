import enum

from app import db, flask_bcrypt


class ProductTransfered(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "scm_product_transfered"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer)
    tgt_id = db.Column(db.String(20))
    created_at = db.Column(db.DATETIME)
