from app.main.stores.jd.api.base import RestApi

class BuildPayRequestRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.shopId = None
			self.orderId = None
			self.source = None
			self.bizToken = None

		def getapiname(self):
			return 'jingdong.buildPayRequest'

			





