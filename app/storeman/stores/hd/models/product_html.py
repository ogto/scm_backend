from app import db, flask_bcrypt


class HDProductHtml(db.Model):
    """ Product HTML for storing product related html contents """
    __tablename__ = "scm_hd_product_html"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    slitmCd = db.Column(db.String(12))
    htmlItstGbdc = db.Column(db.String(2))
    htmlItstCntn = db.Column(db.TEXT)
