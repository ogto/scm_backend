from flask import request
from flask_restx import Resource
from typing import Dict, Tuple

from app.storeman.dtos.group_dto import GroupDto
from app.storeman.services.group_service import get_all_groups, save_new_group, save_group, get_a_group

api = GroupDto.api
_group = GroupDto.group

@api.route('/')
class Groups(Resource):
    @api.doc('user_group_list')
    # @admin_token_required
    @api.response(201, 'List from all user group')
    def get(self):
        """List of all user group"""
        try:
            data = get_all_groups()

            response_object = {
                'status': 'success',
                'message': '',
                'data': data
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'An error occurred while get a user group.',
            }
            return response_object, 200

    @api.expect(_group, validate=True)
    @api.response(201, 'Group successfully created.')
    @api.doc('create a new group')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Store """
        data = request.json
        return save_new_group(data=data)


@api.route('/<group_id>')
class Group(Resource):
    @api.doc('get_a_registered_group')
    def get(self, group_id):
        """
        get a group information by id
        """
        try:
            data = get_a_group(group_id)

            response_object = {
                'status': 'success',
                'message': '',
                'data': data
            }
            return response_object, 201

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'An error occurred while get a user group.',
            }
            return response_object, 200
