from app import db, flask_bcrypt


class Category(db.Model):
    """ Category Model """
    __tablename__ = "scm_jd_category"

    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.Integer)
    indexId = db.Column(db.Integer)
    aliasName = db.Column(db.String(100))
    cat_name = db.Column(db.String(100))
    lev = db.Column(db.Integer)
    cat_status = db.Column(db.Integer)
    created_at = db.Column(db.DATETIME)
