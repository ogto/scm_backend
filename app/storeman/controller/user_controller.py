from flask import render_template, redirect, request, url_for
from flask_restx import Resource
from flask_login import (
    current_user,
    login_user,
    logout_user
)
from sqlalchemy import or_

from app.storeman.models.store import Store
from app.base.models.user import User
from app.storeman.services.auth_service import Auth
from app.storeman.services.blacklist_service import BlacklistToken
from app.storeman.dtos.user_dto import UserDto
from app import db, login_manager
from app.storeman.services.user_service import get_all_users, get_all_usergroup, get_user_by_username, get_user_by_email
from app.storeman.services.store_service import get_a_store
from app.storeman.services.group_service import get_a_group

api = UserDto.api
_user = UserDto.user

@api.route('/')
class Users(Resource):
    @api.doc('user_list')
    # @admin_token_required
    @api.response(201, 'List from all users')
    def get(self):
        """List all registered users"""
        try:
            users = get_all_users()

            response_object = {
                'status': 'success',
                'message': 'User retrieved succesfully.',
                'users': users
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Failed to get all users.',
            }
            return response_object, 409


    parser = api.parser()
    parser.add_argument('param', type=int, help='Some param', location='form')

    @api.response(201, 'Create a user')
    @api.expect(_user, validate=True)
    def post(self):
        """Create new user"""
        post_data = request.json
        username = post_data.get('username')
        email = post_data.get('email')
        store_id = post_data.get('store_id')
        user_group = post_data.get('user_group')

        # Check usename exists
        user = get_user_by_username(username)
        if user:
            response_object = {
                'status': 'fail',
                'message': 'Username already reserved.',
            }
            return response_object, 200

        # Check email exists
        user = get_user_by_email(email)
        if user:
            response_object = {
                'status': 'fail',
                'message': 'Email already exists.',
            }
            return response_object, 200

        # Check store exists
        store = get_a_store(store_id)
        if not store:
            response_object = {
                'status': 'fail',
                'message': 'Store not exists',
            }
            return response_object, 200

        # Check user group exists
        store = get_a_group(user_group)
        if not store:
            response_object = {
                'status': 'fail',
                'message': 'Group not exists',
            }
            return response_object, 200

        # else we can create the user
        user = User(**post_data)
        db.session.add(user)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'User created successfully.',
        }
        return response_object, 201



@api.route('/<username>')
class AUser(Resource):
    @api.response(201, 'Get a user info')
    def get(self, username):
        """ Find a user by name """
        try:
            user = get_user_by_username(username)

            response_object = {
                'status': 'success',
                'message': 'Users retrieved successfully.',
                'data': user
            }
            return response_object, 201

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Faild to retrieve user info.',
            }
            return response_object, 200

