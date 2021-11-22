from flask_restx import Namespace, fields


class GroupDto:
    api = Namespace('groups', description='group related operations')
    group = api.model('groups', {
        'group_name': fields.String(required=True, description='group name'),
        'group_desc': fields.String(required=True, description='group description'),
        'state': fields.String(required=True, description='groups availability'),
    })