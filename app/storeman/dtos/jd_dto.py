from flask_restx import Namespace, fields

class JDDto:
    api = Namespace('jd', description='jd storeman related operations')
    product = api.model('jd_prd', {

    })

    order = api.model('jd_order', {

    })

class JDCategoryDto:
    api = Namespace('jd', description='jd storeman related operations')
    category = api.model('jd_category', {
        "id": fields.Integer(required=True, description='unique id for product'),
        "fid": fields.Integer(required=True, description='unique id for product'),
        "indexId": fields.Integer(required=True, description='unique id for product'),
        "aliasName": fields.Integer(required=False, description='unique id for product'),
        "cat_name": fields.String(required=True, description='unique id for product'),
        "lev": fields.Integer(required=True, description='unique id for product'),
        "cat_status": fields.Integer(required=False, description='unique id for product'),
    })