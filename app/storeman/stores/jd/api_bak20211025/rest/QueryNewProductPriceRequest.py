from app.main.stores.jd.api.base import RestApi

class QueryNewProductPriceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bizToken = None
			self.shopId = None
			self.projectId = None
			self.skuidList = None
			self.source = None

		def getapiname(self):
			return 'jingdong.queryNewProductPrice'

			





