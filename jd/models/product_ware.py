from app import db, flask_bcrypt


class JDProductWare(db.Model):
    """ Product Model """
    __tablename__ = "scm_jd_product_ware"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venderId = db.Column(db.Integer)
    wareId = db.Column(db.Integer)
    title = db.Column(db.String(100))
    categoryId = db.Column(db.Integer)
    multiCategoryId = db.Column(db.Integer)
    brandId = db.Column(db.Integer)
    templateId = db.Column(db.Integer)
    transportId = db.Column(db.Integer)
    wareStatus = db.Column(db.Integer)
    outerId = db.Column(db.String(100))
    itemNum = db.Column(db.String(100))
    barCode = db.Column(db.String(100))
    wareLocation = db.Column(db.Integer)
    delivery = db.Column(db.Integer)
    promiseId = db.Column(db.Integer)
    wrap = db.Column(db.String(100))
    packListing = db.Column(db.String(255))
    length = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    mobileDesc = db.Column(db.String(100))
    introduction = db.Column(db.String(100))
    afterSales = db.Column(db.String(100))
    jdPrice = db.Column(db.DECIMAL(12, 2))
    marketPrice = db.Column(db.DECIMAL(12, 2))
    zhuangBaId = db.Column(db.String(100))
    introductionUseFlag = db.Column(db.String(100))
    mobileZhuangBaId = db.Column(db.String(100))
    mobileDescUseFlag = db.Column(db.String(100))
    designConcept = db.Column(db.String(100))
    fitCaseHtmlApp = db.Column(db.TEXT)
    fitCaseHtmlPc = db.Column(db.TEXT)
