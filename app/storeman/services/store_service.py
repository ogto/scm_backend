import datetime
import json

from app import db
from app.storeman.models.store import Store
from app.storeman.models.store_relations import StoreRelations, StoreFields
from typing import Dict, Tuple

from app.storeman.utils.encoder import AlchemyEncoder


def save_new_store(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    store = Store.query.filter_by(store_id=data['store_id']).first()
    if not store:
        new_store = Store(
            store_id=data['store_id'],
            store_name=data['store_name'],
            store_name_fl=data['store_name_fl'],
            client_id=data['client_id'],
            client_key=data['client_key'],
            response_type=data['response_type'],
            headers=data['headers'],
            etc_1=data['etc_1'] if 'etc_1' in data else '',
            etc_2=data['etc_2'] if 'etc_2' in data else '',
            created_at=datetime.datetime.utcnow()
        )
        save_changes(new_store)

        response_object = {
            'status': 'success',
            'message': 'Store created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Store already exists.',
        }
        return response_object, 200

def save_store(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    store = Store.query.filter_by(store_id=data['store_id']).first()
    if store:
        update_store = Store(
            store_id=data['store_id'],
            store_name=data['store_name'],
            store_name_fl=data['store_name_fl'],
            client_id=data['client_id'],
            client_key=data['client_key'],
            response_type=data['response_type'],
            headers=data['headers'],
            etc_1=data['etc_1'] if 'etc_1' in data else '',
            etc_2=data['etc_2'] if 'etc_2' in data else '',
            updated_at=datetime.datetime.utcnow()
        )
        save_changes(update_store)

        response_object = {
            'status': 'success',
            'message': 'Store updated',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Store already exists.',
        }
        return response_object, 200


def get_all_stores():
    data = Store.query.all()
    if data:
        return json.loads(json.dumps([row.serialize for row in data], cls=AlchemyEncoder))
    else:
        return []


def get_a_store(store_id):
    data = Store.query.filter_by(store_id=store_id).first()
    if data:
        return json.loads(json.dumps(data.serialize, cls=AlchemyEncoder))
    else:
        return {}


def save_changes(data: Store) -> None:
    db.session.add(data)
    db.session.commit()

