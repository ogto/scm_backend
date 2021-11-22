from flask_restx import Namespace, fields


class StoreDto:
    api = Namespace('store', description='store related operations')
    store = api.model('store', {
        'store_id': fields.String(required=True, description='store id'),
        'store_name': fields.String(required=True, description='store name'),
        'store_name_fl': fields.String(required=False, description='store name_fl'),
        'client_id': fields.String(required=False, description='store name_fl'),
        'client_key': fields.String(required=False, description='client key'),
        'response_type': fields.String(required=False, description='response type'),
        'headers': fields.String(required=False, description='headers'),
        'etc-1': fields.String(required=False, description='etc field 1'),
        'etc-2': fields.String(required=False, description='etc field 2'),
    })


class StoreRelationDto:
    api = Namespace('relation', description='store related operations')
    relation = api.model('relation', {
        'op': fields.String(required=True, descrption='operation'),
        'src_id': fields.String(required=True, description='source store id'),
        'tgt_id': fields.String(required=True, description='target store id'),
        'src_table': fields.String(required=True, description='source table'),
        'tgt_table': fields.String(required=True, description='target table'),
    })
