from app import db


class ProductOption(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "scm_product_option"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prd_code = db.Column(db.String, nullable=False)
    opt_code = db.Column(db.String, nullable=False)
    opt_name = db.Column(db.String)
    price = db.Column(db.Numeric(12,2))
    qty = db.Column(db.Integer)
    qty_safe = db.Column(db.Integer)
    thumb_image = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)