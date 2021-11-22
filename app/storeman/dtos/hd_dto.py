from flask_restx import Namespace, fields

class HDDto:
    api = Namespace('hd', description='hyundai storeman related operations')
    product = api.model('hd_prd', {

    })
