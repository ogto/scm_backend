from app import db, flask_bcrypt


class JDProductSku(db.Model):
    """ Product Model """
    __tablename__ = "scm_jd_product_sku"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venderId = db.Column(db.Integer)
    skuId = db.Column(db.Integer)
    jdPrice = db.Column(db.Integer)
    outerId = db.Column(db.String(20))
    stockNum = db.Column(db.String(20))
    barCode = db.Column(db.String(50))
    capacity = db.Column(db.String(50))
