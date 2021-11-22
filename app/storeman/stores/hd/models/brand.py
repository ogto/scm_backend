from app import db, flask_bcrypt


class Brand(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "scm_hd_brand"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venCd = db.Column(db.String(10))
    slitmCd = db.Column(db.String(10))
    sitmCd = db.Column(db.String(10))
    bsitmCd = db.Column(db.String(10))
    slitmNm = db.Column(db.String(100))
    brndCd = db.Column(db.String(20))
    brndNm = db.Column(db.String(100))