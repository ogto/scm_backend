from flask_restx import Namespace, fields


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'id': fields.Integer(required=True, description='unique id for product'),
        'prd_selected': fields.Boolean(required=True, description='selected row', default=False),
        'prd_code': fields.String(required=True, description='store product code'),
        'prd_name_org': fields.String(required=True, description='product original name'),
        'store_id': fields.String(required=False, description='platform type'),
        'prd_img': fields.String(required=False, description='product thumbnail image'),
        'short_desc': fields.String(required=False, description='short description'),
        'price_excluding_tax': fields.Float(required=True, description='price excluding tax'),
        'price': fields.Float(required=True, description='price'),
        'retail_price': fields.Float(required=True, description='retail price'),
        'supply_price': fields.Float(required=True, description='supply price'),
        'prd_condition': fields.String(required=True, description='product condition'),
        'tags': fields.String(required=False, description='hash tags'),
        'tax_type': fields.String(required=True, description='Tax Type'),
        'tax_rate': fields.Float(required=True, description='Tax Rate'),
        'prd_volume': fields.String(required=False, description='product volume'),
        'cat_code': fields.String(required=False, description='Category Code'),
        'prd_desc': fields.String(required=False, description='product description'),
    })

    transfer = api.model('transfer', {
        'prd_code': fields.String(required=True, description='store product code'),
    })
