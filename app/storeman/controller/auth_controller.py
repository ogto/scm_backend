import json

from flask import request
from flask_restplus import Resource
from app.storeman.services.auth_service import Auth
from app.storeman.services.user_service import get_user_by_id
from app.storeman.dtos.user_dto import AuthDto
from app import login_manager
from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import logging
from ..utils.encoder import AlchemyEncoder

api = AuthDto.api
user_auth = AuthDto.user_auth
logger = logging.getLogger()

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        ret_obj = Auth.login_user(post_data)
        if 200 == ret_obj[1]:
            user = ret_obj[0].pop("user")
            login_user(user)

        return ret_obj[0]


@api.route('/logout')
class UserLogout(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
