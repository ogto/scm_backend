from app import db
from app.storeman.utils.helpers import format_datetime


class Menu(db.Model):
    __tablename__ = 'scm_user_menu'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_seq = db.Column(db.String(50))
    menu_name = db.Column(db.String(100))
    menu_directory = db.Column(db.String(50))
    menu_controller = db.Column(db.String(50))
    menu_method = db.Column(db.String(50))
    menu_heading = db.Column(db.String(200))
    menu_desc = db.Column(db.TEXT)
    menu_icon = db.Column(db.String(30))
    state = db.Column(db.String(1), default='Y')
    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'menu_seq': self.menu_seq,
            'menu_name': self.menu_name,
            'menu_directory': self.menu_directory,
            'menu_controller': self.menu_controller,
            'menu_method': self.menu_method,
            'menu_heading': self.menu_heading,
            'menu_desc': self.menu_desc,
            'menu_icon': self.menu_icon,
            'state': self.state,
            'created_at': format_datetime(self.created_at),
            'updated_at': format_datetime(self.updated_at)
        }
