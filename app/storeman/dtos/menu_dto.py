from flask_restx import Namespace, fields


class MenuDto:
    api = Namespace('menus', description='menu related operations')
    menu = api.model('menus', {
        'menu_seq': fields.String(required=True, description='menu sequence like A01, A0101'),
        'menu_name': fields.String(required=True, description='menu name'),
        'menu_directory': fields.String(required=False, description='menu path'),
        'menu_controller': fields.String(required=False, description='menu controller'),
        'menu_method': fields.String(required=False, description='menu method'),
        'menu_heading': fields.String(required=False, description='menu heading'),
        'menu_desc': fields.String(required=False, description='menu description'),
        'menu_icon': fields.String(required=False, description='menu icon'),
        'state': fields.String(required=True, description='menu availability Y/N'),
    })