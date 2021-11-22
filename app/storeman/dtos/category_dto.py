from flask_restx import Namespace, fields


class CategoryDto:
    api = Namespace('category', description='category related operations')
    category = api.model('category', {
        'id': fields.Integer(required=True, description='unique id for category'),
        'category_no': fields.Integer(required=True),
        'category_depth': fields.Integer(required=True, default=1),
        'parent_category_no': fields.Integer(required=False),
        'category_name': fields.String(required=True),
        'display_type': fields.String(required=True),
        'full_category_no': fields.String(required=True),
        'full_category_name': fields.String(required=True),
        'use_main': fields.String(required=True),
        'use_display': fields.String(required=True),
        'display_order': fields.Integer(required=True),
        'soldout_product_display': fields.String(required=True),
        'sub_category_product_display': fields.String(required=True, default='F'),
        'hashtag_product_display': fields.String(required=True, default='T'),
        'product_display_scope': fields.String(required=True, default='A'),
        'product_display_type': fields.String(required=True, default='U'),
        'product_display_key': fields.String(required=True, default='A'),
        'product_display_sort': fields.String(required=True, default='D'),
        'product_display_period': fields.String(required=True, default='W'),
        'normal_product_display_type': fields.String(required=False),
        'normal_product_display_key': fields.String(required=False),
        'normal_product_display_sort': fields.String(required=False),
        'normal_product_display_period': fields.String(required=False),
        'recommend_product_display_type': fields.String(required=False),
        'recommend_product_display_key': fields.String(required=False),
        'recommend_product_display_sort': fields.String(required=False),
        'recommend_product_display_period': fields.String(required=False),
        'new_product_display_type': fields.String(required=False),
        'new_product_display_key': fields.String(required=False),
        'new_product_display_sort': fields.String(required=False),
        'new_product_display_period': fields.String(required=False),
        'access_authority': fields.String(required=False, default='T')
    })
