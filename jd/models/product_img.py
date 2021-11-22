from app import db, flask_bcrypt


class JDProductImg(db.Model):
    """ Product Image Model """
    __tablename__ = "scm_jd_product_img"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wareId = db.Column(db.Integer)
    outerId = db.Column(db.String(20))
    colorId = db.Column(db.String(10))
    imgIndex = db.Column(db.Integer)
    imgUrl = db.Column(db.String(255))
    imgZoneId = db.Column(db.String(100))
