from app import db, flask_bcrypt


class HDProductPrice(db.Model):
    """ Product HTML for storing product related html contents """
    __tablename__ = "scm_hd_product_price"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slitmCd = db.Column(db.String(12))
    prcAthzSeq = db.Column(db.Integer)
    prcAplyStrtDtm = db.Column(db.String(8))
    sellPrc = db.Column(db.Integer)
    prchPrc = db.Column(db.Integer)
    mrgnRate = db.Column(db.Integer)
    wintInsmMths = db.Column(db.Integer)
    csmPrc = db.Column(db.Integer)
    svmtPrdcYn = db.Column(db.String(1))
    spymDcAmt = db.Column(db.Integer)
    spymDcYn = db.Column(db.String(1))
    gnrlCopnNo = db.Column(db.String(20))
    svmtRate = db.Column(db.Integer)
    svmt = db.Column(db.Integer)
    prcDcEndDtm = db.Column(db.String(8))
    stplMths = db.Column(db.Integer)
    insmMths = db.Column(db.Integer)
    venItemCd = db.Column(db.String(10))
    dptsVenOpCd = db.Column(db.String(10))
    dptsVenSaleCd = db.Column(db.String(10))
