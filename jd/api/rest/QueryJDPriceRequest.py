from jd.api.base import RestApi

class QueryJDPriceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bizToken = None
			self.shopId = None
			self.projectId = None
			self.skuidList = None
			self.source = None

		def getapiname(self):
			return 'jingdong.queryJDPrice'

			





