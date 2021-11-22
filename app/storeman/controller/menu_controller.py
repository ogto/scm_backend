from flask import request
from flask_restx import Resource
from typing import Dict, Tuple

from app.storeman.dtos.menu_dto import MenuDto
from app.storeman.services.menu_service import get_all_menus, save_new_menu, save_menu, get_a_menu

api = MenuDto.api
_menu = MenuDto.menu

@api.route('/')
class Menus(Resource):
    @api.doc('menu_list')
    @api.response(201, 'List from all menu')
    def get(self):
        """List of all menu"""
        try:
            data = get_all_menus()

            response_object = {
                'status': 'success',
                'message': '',
                'data': data
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'An error occurred while get a menu.',
            }
            return response_object, 200

    @api.expect(_menu, validate=True)
    @api.response(201, 'Menu successfully created.')
    @api.doc('create a new menu')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Store """
        data = request.json
        return save_new_menu(data=data)


@api.route('/<menu_seq>')
class Menu(Resource):
    @api.doc('get_a_registered_menu')
    def get(self, menu_seq):
        """
        get a menu information by seq
        """
        try:
            data = get_a_menu(menu_seq)

            response_object = {
                'status': 'success',
                'message': '',
                'data': data
            }
            return response_object, 201

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'An error occurred while get a menu.',
            }
            return response_object, 200


    @api.expect(_menu, validate=True)
    @api.doc('update_a_registerd_menu')
    @api.response(201, 'Menu successfully created.')
    def put(self) -> Tuple[Dict[str, str], int]:
        """ Update a registerd menu """
        data = request.json
        return save_menu(data=data)
