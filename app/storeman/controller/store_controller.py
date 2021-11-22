from flask import request
from flask_restx import Resource

from app.storeman.dtos.store_dto import StoreDto, StoreRelationDto
from app.storeman.services.store_service import save_new_store, get_all_stores, get_a_store
from typing import Dict, Tuple

api = StoreDto.api
_store = StoreDto.store
_relation = StoreRelationDto.relation

@api.route('/')
class StoreList(Resource):
    @api.doc('list_of_registered_stores')
    def get(self):
        """List all registered stores"""
        try:
            data = get_all_stores()

            response_object = {
                'status': 'success',
                'message': 'Stores retrieved successfully.',
                'data': data
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Failed to get stores.',
            }
            return response_object, 200


    @api.expect(_store, validate=True)
    @api.response(201, 'Store successfully created.')
    @api.doc('create a new store')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Store """
        data = request.json
        return save_new_store(data=data)


@api.route('/<store_id>')
class Store(Resource):
    @api.doc('get_a_registered_store')
    def get(self, store_id):
        """
        get a store information by id
        """
        try:
            data = get_a_store(store_id)

            response_object = {
                'status': 'success',
                'message': 'Stores retrieved successfully.',
                'data': data
            }
            return response_object, 201

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Failed to get stores.',
            }
            return response_object, 200
