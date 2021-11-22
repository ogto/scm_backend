from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import db
from app.base.util import hash_pass
from app.storeman.utils.helpers import format_datetime

class Group(db.Model):

    __tablename__ = 'scm_user_group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(100))
    group_desc = db.Column(db.TEXT)
    state = db.Column(db.String(1), nullable=False, default='Y')
    scm_user = relationship("User", back_populates="group_rel")
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'group_name': self.group_name,
            'group_desc': self.group_desc,
            'state': self.state,
            'created_at': format_datetime(self.created_at),
            'updated_at': format_datetime(self.updated_at)
        }