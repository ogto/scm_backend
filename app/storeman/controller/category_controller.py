from flask import request
from flask_restx import Resource

from app.storeman.dtos.jd_dto import JDCategoryDto
from app.storeman.dtos.category_dto import CategoryDto
from app.storeman.services.product_service import save_new_product, get_all_products, pull_products, get_store_products, \
    transfer_product, update_products_stock
from app.storeman.services.category_service import get_all_categories, get_store_categories
from typing import Dict, Tuple

from jd.service.jd_service import save_new_category

api = CategoryDto.api
_category = CategoryDto.category

@api.route('/')
class Category(Resource):
    @api.doc('list_of_scm_category_list')
    def get(self):
        """List all categories"""
        try:
            data = get_all_categories()

            response_object = {
                'status': 'success',
                'message': 'Category retrieves Successfully!',
                'data': data
            }
            return response_object, 200
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'No category found.',
            }
            return response_object, 200


    @api.doc('save_new_scm_category')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new category """
        data = request.json
        return save_new_category(data=data)


@api.route('/<store_id>')
@api.param('store_id', 'The store identifier')
class StoreCategory(Resource):
    @api.doc('list_of_store_categories')
    # @admin_token_required
    # @api.marshal_list_with(_jd_category, envelope='data')
    def get(self, store_id):
        """List all registered users"""
        # store_id = request.args.get('store_id')
        return get_store_categories(store_id)
