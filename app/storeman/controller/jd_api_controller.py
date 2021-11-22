from flask import request
from flask_restx import Resource

from app.storeman.dtos.jd_dto import JDDto
from app.storeman.apis import get_product_list, post_new_product, update_product, delete_product, get_product, \
    get_approved_brand, get_valid_categorys, find_attrs_unlimitCate, get_sku, get_sku_list, get_transport_template_list, \
    find_values_attrIdUnlimit
from app.storeman.apis import get_order_list, get_order

api = JDDto.api
_product = JDDto.product
_order = JDDto.order


@api.route('/product')
class JDProductList(Resource):
    @api.doc('list_of_jingdong_products')
    @api.param('page', 'Page Number')
    @api.param('size', 'Page size')
    # @admin_token_required
    @api.response(201, 'List from jingdong storeman products')
    def get(self):
        """
        List all jd's products
        """
        page = request.args.get('page')
        size = request.args.get('size')
        return get_product_list(int(page), int(size))

    @api.doc('post_new_product')
    # @admin_token_required
    @api.response(201, 'product registered successfully')
    def post(self):
        """
        List all jd's products
        """
        data = request.json
        post_new_product(data)

@api.route('/brand')
@api.param('brandname')
@api.response(404, 'Brand not found.')
class JDVenderBrand(Resource):
    @api.doc('approved_venders_brands')
    @api.response(201, 'approved vender brands')
    def get(self):
        """
        jd's approved brand
        """
        brandname = request.args.get("brandname")
        return get_approved_brand(brandname)

@api.route('/skulist')
class JDProductList(Resource):
    @api.doc('list_of_jingdong_products sku')
    @api.param('page', 'Page Number')
    @api.param('size', 'Page size')
    # @admin_token_required
    @api.response(201, 'List from jingdong storeman products')
    def get(self):
        """
        List all jd's products
        """
        page = request.args.get('page')
        size = request.args.get('size')
        return get_sku_list(int(page), int(size))

@api.route('/sku/<skuid>')
@api.response(404, 'SKU not found.')
class JDSku(Resource):
    @api.doc('Skus')
    @api.response(201, 'Skus')
    def get(self,skuid):
        """
        get full valid skus bu id
        """
        return get_sku(skuid)


@api.route('/category')
@api.response(404, 'Brand not found.')
class JDValidCategory(Resource):
    @api.doc('valid_categorys')
    @api.response(201, 'valid categorys')
    def get(self):
        """
        get full valid categorys by vendor ID
        """
        return get_valid_categorys()


@api.route('/transport')
@api.response(404, 'Transport template not found.')
class JDTransportList(Resource):
    @api.doc('transport_template')
    @api.response(201, 'trnasportid')
    def get(self):
        """
        get transport template list
        """
        return get_transport_template_list()


@api.route('/attr')
@api.response(404, 'Brand not found.')
class JDValidCategory(Resource):
    @api.doc('attributes')
    @api.param('cid', 'category id')
    @api.param('type', 'category type')
    @api.response(201, 'attibutes')
    def get(self):
        """
        get full valid categorys by vendor ID
        """
        cid = request.args.get("cid")
        type = request.args.get("type")
        return find_attrs_unlimitCate(cid, type)


@api.route('/attrvalues')
@api.response(404, 'Attribute value not found.')
class JDAttributeValues(Resource):
    @api.doc('attribute_values')
    @api.param('categoryAttrId', 'category attribute id')
    @api.response(201, 'attibutes')
    def get(self):
        """
        get full valid categorys by vendor ID
        """
        cai = request.args.get("categoryAttrId")
        return find_values_attrIdUnlimit(cai)


@api.route('/product/<product_id>')
@api.param('product_id', 'The Product identifier')
@api.response(404, 'Product not found.')
class JDProduct(Resource):
    @api.doc('jingdong_products detail')
    # @admin_token_required
    @api.response(201, 'jingdong products detail')
    def get(self, product_id):
        """
        jd's products detail
        """
        return get_product(product_id)


    @api.doc('update_product_detail')
    # @admin_token_required
    @api.response(201, 'product updated successfully')
    def put(self):
        """
        Update product
        """
        return update_product()

    @api.doc('delete_a_product')
    # @admin_token_required
    @api.response(201, 'product deleted successfully')
    def delete(self):
        """
        delete a product
        """
        return delete_product()


@api.route('/order')
class JDOrderList(Resource):
    @api.doc('list_of_jingdong_orders')
    # @admin_token_required
    @api.response(201, 'List from jingdong storeman orders')
    def get(self):
        """
        List all jd's orders
        """
        return get_order_list()

@api.route('/order/<order_id>')
@api.param('order_id', 'The order identifier')
@api.response(404, 'order not found.')
class JDOrder(Resource):
    @api.doc('jingdong_order')
    # @admin_token_required
    @api.response(201, 'jingdong storeman order')
    def get(self, order_id):
        """
        List all jd's orders
        """
        return get_order(order_id=order_id)

    @api.doc('update_order_detail')
    # @admin_token_required
    @api.response(201, 'order updated successfully')
    def put(self):
        """
        Update product
        """
        return update_order()

    @api.doc('delete_a_order')
    # @admin_token_required
    @api.response(201, 'order deleted successfully')
    def delete(self):
        """
        delete an order
        """
        return delete_order()
