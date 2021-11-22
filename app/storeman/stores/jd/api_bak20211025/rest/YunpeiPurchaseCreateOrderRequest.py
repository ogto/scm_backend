from app.main.stores.jd.api.base import RestApi

class YunpeiPurchaseCreateOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.address_detail = None
			self.mobile = None
			self.city_name = None
			self.seller_request_list = None

		def getapiname(self):
			return 'jingdong.yunpei.purchase.createOrder'

			





