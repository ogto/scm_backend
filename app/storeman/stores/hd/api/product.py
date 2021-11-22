import base64

import requests
import json

class Product(object):
    config = Config()
    version = config.CONFIG['VERSION']

    def get_product(self, access_token, mall_id, mall_productno):
        url = "https://" + mall_id + f".cafe24api.com/api/v2/admin/products/{mall_productno}".format(mall_productno=mall_productno)
        res = self.send_request(url, 'GET', access_token=access_token, version=self.version)
        return res

    def create_product(self, access_token, mall_id, payload):
        url = "https://" + mall_id + f".cafe24api.com/api/v2/admin/products"
        res = self.send_request(url, 'POST', access_token=access_token, version=self.version, data=payload)
        return res

    def update_product(self, access_token, mall_id, payload):
        url = "https://" + mall_id + f".cafe24api.com/api/v2/admin/products"
        res = self.send_request(url, 'PUT', access_token=access_token, version=self.version, data=payload)
        return res

    def get_product_variants(self, access_token, mall_id, mall_product_id):
        url = "https://" + mall_id + f".cafe24api.com/api/v2/admin/products/" + str(mall_product_id) + "/variants"
        res = self.send_request(url, 'GET', access_token=access_token, version=self.version)
        return res

    def update_product_variants(self, access_token, mall_id, mall_product_id, payload):
        url = "https://" + mall_id + f".cafe24api.com/api/v2/admin/products/" + str(mall_product_id) + "/variants"
        res = self.send_request(url, 'PUT', access_token=access_token, version=self.version, data=payload)
        return res

    def update_product_status(self, access_token, mall_id, product_no, mall_product_no, code='Y'):
        if mall_product_no == "":
            return None
        _resJson = self.get_product()

    def get_image_as_base64(self, url):
        return base64.b64encode( requests.get(url).content)

    def upload_product_image(self, access_token, mall_id, img_path):
        url = "https://" + mall_id + f".cafe24api.com/api/v2/admin/products/images"
        _params = {}
        encoded_image = self.get_image_as_base64(img_path)
        _params["requests"] = [
            {"image": encoded_image.decode()}
        ]
        payload = json.dumps(_params)

        res = self.send_request(url, 'POST', access_token=access_token, version=self.version, data=payload)
        if res.status_code // 200 == 1:
            img_data = json.loads(res.text)
            ret_path = helper.stripslashes(img_data["images"][0]["path"]).replace("http://" + mall_id + ".cafe24.com", "")
            print(ret_path)
            return ret_path
        else:
            return None

    def make_trans_data(self, access_token, mall_id, prd_data):
        _params = {}
        _params["shop_no"] = 1
        _params["request"] = {}

        _request = {}
        _request["display"] = "T"
        _request["selling"] = "T"
        _request["product_condition"] = "N"
        _request["custom_product_code"] = prd_data['row']['CD_STYLE']
        _request["product_name"] = prd_data['row']['DS_STYLE']
        _request["eng_product_name"] = prd_data['row']['DS_STYLEEN']
        _request["supply_product_name"] = prd_data['row']['DS_STYLE']
        _request["price"] = prd_data['price']['selPrc']
        _request["retail_price"] = prd_data['price']['selPrc']
        _request["supply_price"] = prd_data['price']['originPrc']
        _request["has_option"] = "T"
        _request["options"] = prd_data["optionData"]
        _request["image_upload_type"] = "A"

        detail_image = self.upload_product_image(access_token, mall_id, prd_data["mainImageData"])
        if detail_image:
            _request["detail_image"] = detail_image

        _request["buy_unit_type"] = "O"
        _request["buy_unit"] = 1
        _request["order_quantity_limit_type"] = "O"
        _request["minimum_quantity"] = 1
        _request["maximum_quantity"] = 0
        _request["points_by_product"] = "F"
        _request["except_member_points"] = "F"

        ## description
        _request["description"] = prd_data['html_description']
        _request["mobile_description"] = prd_data['html_description']
        _request["summary_description"] = prd_data['shortDescription']
        _request["simple_description"] = prd_data['shortDescription']

        ## infomations
        _request["payment_info"] = "Sample payment info. You have to Pay."
        _request["shipping_info"] = "Sample shipping info. You have to ship."
        _request["exchange_info"] = "Sample exchange info. You have to exchange."
        _request["service_info"] = "Sample service info. You have to service."

        _request["hscode"] = prd_data["row_first"]["CD_HSCODE"]

        _request["shipping_scope"] = "A"
        _request["shipping_fee_by_product"] = "T"
        _request["shipping_method"] = "01"
        _request["shipping_period"] = {
                                          "minimum": 7,
                                          "maximum": 14
                                      },
        _request["shipping_area"] = "All around world"
        _request["shipping_fee_type"] = "R"
        _request["clearance_category_code"] = None
        _request["shipping_rates"] = [
            {
               "shipping_fee": prd_data["price"]["transPrc"]
            }
        ]
        _request["tax_type"] = "A"
        _request["tax_amount"] = 10
        _request["prepaid_shipping_fee"] = "P"
        _request["origin_classification"] = "T"
        _request["origin_place_no"] = 264
        _request["made_in_code"] = 'CN'

        _params["request"] = _request
        return _params
