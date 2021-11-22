from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'store_id': fields.String(required=True, description='user store id'),
        'user_group': fields.String(required=True, description='user group id')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })
