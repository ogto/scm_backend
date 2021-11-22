from app.main.stores.jd.api.base import RestApi

class YunpeiPurchaseAddressAddRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.province = None
			self.city = None
			self.district = None
			self.street = None
			self.address = None
			self.consignee = None
			self.mobile = None
			self.is_default = None

		def getapiname(self):
			return 'jingdong.yunpei.purchase.address.add'

			





