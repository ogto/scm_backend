import datetime
import json

from app import db
from typing import Dict, Tuple
from sqlalchemy import or_

from app.base.models.menu import Menu
from app.storeman.utils.encoder import AlchemyEncoder


def save_new_menu(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    menu = Menu.query.filter(or_(Menu.menu_seq == data['menu_seq'])).first()

    if not menu:
        new_menu = Menu(
            menu_seq=data['menu_seq'],
            menu_name=data['menu_name'],
            menu_directory=data['menu_directory'],
            menu_controller=data['menu_controller'],
            menu_method=data['menu_method'],
            menu_heading=data['menu_heading'],
            menu_desc=data['menu_desc'],
            menu_icon=data['menu_icon']
        )
        save_changes(new_menu)

        response_object = {
            'status': 'success',
            'message': 'Menu created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Menu seq already exists.',
        }
        return response_object, 200


def save_menu(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    menu = Menu.query.filter_by(menu_seq=data['menu_seq']).first()
    if menu:
        update_menu = Menu(
            menu_seq=data['menu_seq'],
            menu_name=data['menu_name'],
            menu_directory=data['menu_directory'],
            menu_controller=data['menu_controller'],
            menu_method=data['menu_method'],
            menu_heading=data['menu_heading'],
            menu_desc=data['menu_desc'],
            menu_icon=data['menu_icon'],
            updated_at=datetime.datetime.utcnow()
        )
        save_changes(update_menu)

        response_object = {
            'status': 'success',
            'message': 'Menu updated',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Menu update failed.',
        }
        return response_object, 200


def get_all_menus():
    data = Menu.query.all()
    return json.loads(json.dumps([row.serialize for row in data], cls=AlchemyEncoder))


def get_a_menu(menu_seq):
    data = Menu.query.filter_by(menu_seq=menu_seq).first()
    return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))


def save_changes(data: any) -> None:
    db.session.add(data)
    db.session.commit()

