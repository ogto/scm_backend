import json

from app.base.models.user import User
from app.storeman.services.blacklist_service import save_token
from typing import Dict, Tuple

from ..utils.encoder import AlchemyEncoder
from ...base.util import verify_pass

class Auth:
    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = User.query.filter_by(username=data.get('username')).first()
            if user and user.check_password(data.get('password')):
            # if user and verify_pass(data.get('password'),user.password):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token,
                        'user': user
                        # 'user': json.loads(json.dumps(user, cls=AlchemyEncoder))
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 200

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 200

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'created_at': str(user.created_at)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 200
