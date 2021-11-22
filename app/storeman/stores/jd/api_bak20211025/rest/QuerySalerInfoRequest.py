from app.main.stores.jd.api.base import RestApi

class QuerySalerInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bizToken = None
			self.source = None
			self.shopId = None

		def getapiname(self):
			return 'jingdong.querySalerInfo'

			





