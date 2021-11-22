import datetime
import json

from app import db
from app.base.models.user import User
from typing import Dict, Tuple
from sqlalchemy import or_
from flask import jsonify

from app.base.models.group import Group
from app.storeman.models.store import Store
from app.storeman.utils.encoder import AlchemyEncoder


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter(or_(User.username==data['username'], User.email==data['email'])).first()

    if not user:
        new_user = User(
            username=data['username'],
            email=data['email'],
            store_id=data['store_id'],
            user_group=int(data['user_group'])
        )
        new_user.password = data['password']
        save_changes(new_user)

        response_object = {
            'status': 'success',
            'message': 'User created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.',
        }
        return response_object, 200


def save_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(username=data['username']).first()
    if user:
        update_user = User(
            username=data['username'],
            email=data['email'],
            store_id=data['store_id'],
            user_group=int(data['user_group'])
        )
        save_changes(update_user)

        response_object = {
            'status': 'success',
            'message': 'User updated',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.',
        }
        return response_object, 200


def get_all_users():
    data = User.query.all()
    if data:
        return json.loads(json.dumps([item.serialize for item in data], cls=AlchemyEncoder))
    else:
        return []
    # return jsonify(json_list=[dict(row.items()) for row in data])


def get_all_usergroup():
    data = Group.query.all()
    return json.loads(json.dumps(data, cls=AlchemyEncoder))


def get_select_usergroup():
    data = Group.query.all()
    return json.loads(json.dumps(data, cls=AlchemyEncoder))


def get_a_user(username):
    data = User.query.filter_by(username=username).first()
    if data:
        return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))
    else:
        return {}


def get_user_by_id(id):
    data = User.query.filter_by(id=id).first()
    if data:
        return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))
    else:
        return {}


def get_user_by_username(username):
    data = User.query.filter_by(username=username).first()
    if data:
        return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))
    else:
        return {}


def get_user_by_email(email):
    data = User.query.filter_by(email=email).first()
    if data:
        return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))
    else:
        return {}


def get_user_storeinfo(id):
    data = {}
    user = User.query.filter_by(id=id).first()
    if user:
        data = Store.query.filter_by(id=user.store_id).first()
    return json.loads(json.dumps(data, cls=AlchemyEncoder))


def save_changes(data: any) -> None:
    db.session.add(data)
    db.session.commit()

