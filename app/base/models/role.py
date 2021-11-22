from app import db

class Role(db.Model):

    __tablename__ = 'scm_user_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    user_menu_id = db.Column(db.Integer)
    p_read = db.Column(db.String(1), nullable=False, default='N')
    p_write = db.Column(db.String(1), nullable=False, default='N')
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)
