import datetime
import json

from app import db
from typing import Dict, Tuple
from sqlalchemy import or_

from app.base.models.group import Group
from app.base.models.role import Role
from app.storeman.utils.encoder import AlchemyEncoder


def save_new_group(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    group = Group.query.filter(or_(Group.group_name==data['groupname'])).first()

    if not group:
        new_group = Group(
            group_name=data['groupname'],
            group_desc=data['desc']
        )
        save_changes(new_group)

        response_object = {
            'status': 'success',
            'message': 'Group created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Group already exists.',
        }
        return response_object, 200


def save_group(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    group = Group.query.filter_by(group_name=data['groupname']).first()
    if group:
        update_group = Group(
            group_name=data['groupname'],
            group_desc=data['desc'],
            updated_at=datetime.datetime.utcnow()
        )
        save_changes(update_group)

        response_object = {
            'status': 'success',
            'message': 'Group updated',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Group update failed.',
        }
        return response_object, 200


def get_all_groups():
    data = Group.query.all()
    return json.loads(json.dumps([row.serialize for row in data], cls=AlchemyEncoder))


def get_a_group(group_id):
    if isinstance(group_id, str):
        group_id = int(group_id)
    data = Group.query.filter_by(id=group_id).first()
    if data:
        return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))
    else:
        return None


def get_all_groups_with_permission():
    data = Group.query.all()
    return json.loads(json.dumps(data, cls=AlchemyEncoder))


def save_changes(data: any) -> None:
    db.session.add(data)
    db.session.commit()

