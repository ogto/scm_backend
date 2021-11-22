import enum

from app import db, flask_bcrypt
from app.storeman.utils.helpers import format_datetime


class EnumResType(enum.Enum):
    JSON = 'JSON'
    XML = 'XML'
    TEXT = 'Text'


class Store(db.Model):
    """ Store Model for storing store related details """
    __tablename__ = "scm_store"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.String(10), nullable=False, unique=True)
    store_name = db.Column(db.String(100), nullable=True)
    store_name_fl = db.Column(db.String(100), nullable=True)
    client_id = db.Column(db.String(100), nullable=True)
    client_key = db.Column(db.String(200), nullable=True)
    response_type = db.Column(db.Enum(EnumResType), default=EnumResType.JSON)
    headers = db.Column(db.Text, nullable=True)
    etc_1 = db.Column(db.Text, nullable=True)
    etc_2 = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'store_id': self.store_id,
            'store_name': self.store_name,
            'store_name_fl': self.store_name_fl,
            'client_id': self.client_id,
            'client_key': self.client_key,
            'response_type': self.response_type.value,
            'headers': self.headers,
            'etc_1': self.etc_1,
            'etc_2': self.etc_2,
            'created_at': format_datetime(self.created_at),
            'updated_at': format_datetime(self.updated_at)
        }