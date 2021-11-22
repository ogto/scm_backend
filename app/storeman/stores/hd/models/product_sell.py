from app import db, flask_bcrypt


class HDProductSell(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "scm_hd_product_sell"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bsitmCd = db.Column(db.String(20))
    slitmCd = db.Column(db.String(20))
    uitmCd = db.Column(db.String(10))
    uitmTmpCd = db.Column(db.String(10))
    uitmClrGbcd = db.Column(db.String(10))
    uitmSizeCd = db.Column(db.String(10))
    uitmPatnGbcd = db.Column(db.String(10))
    uitmItemFormCd = db.Column(db.String(10))
    uitm1AttrNm = db.Column(db.String(50))
    uitm2AttrNm = db.Column(db.String(50))
    uitm3AttrNm = db.Column(db.String(50))
    uitm4AttrNm = db.Column(db.String(50))
    uitmEtcNm = db.Column(db.String(50))
    uitmTotNm = db.Column(db.String(50))
    sellGbcd = db.Column(db.String(2))
    sellStrtDt = db.Column(db.String(8))
    sellEndDt = db.Column(db.String(8))
    uitmStckSeq = db.Column(db.Integer)
    maxSellPossQty = db.Column(db.Integer)
    oldMaxSellPossQty = db.Column(db.Integer)
    totSellQty = db.Column(db.Integer)
    uitm1HexClrVal = db.Column(db.String(100))
    uitm2HexClrVal = db.Column(db.String(100))
    uitm3HexClrVal = db.Column(db.String(100))
    uitm4HexClrVal = db.Column(db.String(100))
    imgNm = db.Column(db.String(100))
    remainQty = db.Column(db.Integer)
