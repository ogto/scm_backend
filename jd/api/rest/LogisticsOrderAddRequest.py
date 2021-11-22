from jd.api.base import RestApi

class LogisticsOrderAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channels_seller_no = None
			self.channels_outbound_no = None
			self.warehouse_no = None
			self.carriers_id = None
			self.expect_date = None
			self.order_no = None
			self.shop_no = None
			self.consignee_name = None
			self.address_province = None
			self.address_city = None
			self.address_county = None
			self.address_town = None
			self.address = None
			self.zip_code = None
			self.phone = None
			self.mobile = None
			self.receivable = None
			self.email = None
			self.buyer_remark = None
			self.verify_remark = None
			self.return_consignee_address = None
			self.return_consignee_name = None
			self.return_consignee_phone = None
			self.station_no = None
			self.station_name = None
			self.order_mark = None
			self.shop_order_source = None
			self.shop_order_create_time = None
			self.picker = None
			self.picker_call = None
			self.piker_id = None
			self.pack_type = None
			self.goods_no = None
			self.sku_id = None
			self.shopGoodsNo = None
			self.qty = None
			self.goods_status = None

		def getapiname(self):
			return 'jingdong.logistics.order.add'

			





