from app import db, flask_bcrypt


class JDBrands(db.Model):
    """ Product Model """
    __tablename__ = "scm_jd_brand"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    erpBrandId = db.Column(db.Integer)
    brandName = db.Column(db.String(100))
