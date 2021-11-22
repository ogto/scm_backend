from flask import request
from flask_restx import Resource

from app.storeman.dtos.jd_dto import JDCategoryDto
from app.storeman.dtos.product_dto import ProductDto
from app.storeman.services.product_service import save_new_product, get_all_products, pull_products, get_store_products, \
    transfer_product, update_products_stock, get_stores_products
from app.storeman.services.category_service import get_all_categories
from typing import Dict, Tuple

api = ProductDto.api
_product = ProductDto.product
_jd_category = JDCategoryDto.category
_prd_transfer = ProductDto.transfer
@api.route('/')
class ProductList(Resource):
    @api.doc('list_of_scm_product_list')
    @api.response(201, 'List from all products')
    def get(self):
        """List all scm products"""
        try:
            prds = get_all_products()

            if not prds:
                prds = None

            response_object = {
                'status': 'success',
                'message': 'Products retrieved successfully',
                'products': prds
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Failed to get all products.',
            }
            return response_object, 200

    @api.expect(_product, validate=True)
    @api.response(201, 'product registerd successfully')
    @api.doc('create a new product')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Product """
        data = request.json
        return save_new_product(data=data)


@api.route('/updatestock/<store_id>')
class ProductStock(Resource):
    @api.doc('list_of_scm_product_list')
    # @admin_token_required
    @api.marshal_list_with(_product, envelope='data')
    def put(self):
        """List all registered users"""
        store_id = request.args.get('store_id')
        return update_products_stock(store_id)


@api.route('/<store_id>')
@api.response(404, 'Product not found.')
class StoreProductList(Resource):
    @api.doc('list_of_store_product_list')
    def get(self, store_id):
        """List all registered products"""
        try:
            prds = get_stores_products(store_id)

            response_object = {
                'status': 'success',
                'message': 'Users retrieved successfully.',
                'data': prds
            }
            return response_object, 201

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Failed to get stores products.',
            }
            return response_object, 200


@api.route('/pull')
class ProductPullFromStore(Resource):
    @api.doc('pull_product_info_from_a_stores')
    def post(self):
        """
        Pull Products from A partner store
        """
        return pull_products()


@api.route('/transfer', methods=['POST'])
@api.param('store_id')
@api.param('store_code')
class ProductTransfer(Resource):
    @api.doc('tranfer_product')
    @api.expect(_prd_transfer, validate=True)
    def post(self) -> (Tuple[Dict[str, str], int]):
        """Pull Products from A partner store"""
        data = request.json
        # tgt = data.get("store_code")
        tgt = request.args.get('store_code')
        states = data.get("prd_code")

        if len(states) < 1:
            response_object = {
                'status': 'fail',
                'message': 'no selected product',
            }
            return response_object, 200

        # src = states[0]['store_id']
        src = request.args.get('store_id')
        prd_list = []
        # for prd in states:
        #     print(prd)
            # prd_list.append(prd)
        # print(prd_list)
        return transfer_product(src, tgt, states)
