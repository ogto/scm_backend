from app import db, flask_bcrypt


class HDProductImg(db.Model):
    """ Product Images for storing product related images """
    __tablename__ = "scm_hd_product_img"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slitmCd = db.Column(db.String(12))
    slitmImgSeq = db.Column(db.Integer)
    imgLblNm = db.Column(db.String(10))
    orglImgNm = db.Column(db.String(100))
    trndhImgNm = db.Column(db.String(100))
    sImgNm = db.Column(db.String(100))
    mImgNm = db.Column(db.String(100))
    lImgNm = db.Column(db.String(100))
    enlg1ImgNm = db.Column(db.String(100))
    enlg2ImgNm = db.Column(db.String(100))
    enlg3ImgNm = db.Column(db.String(100))
    enlg1ImgSize = db.Column(db.String(4))
    enlg2ImgSize = db.Column(db.String(4))
    enlg3ImgSize = db.Column(db.String(4))
