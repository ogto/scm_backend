from jd.api.base import RestApi

class QueryPurchaseProductRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.shopId = None
			self.projectId = None
			self.index = None
			self.pageSize = None
			self.bizToken = None
			self.source = None
			self.modiStartTime = None
			self.modiEndTime = None

		def getapiname(self):
			return 'jingdong.queryPurchaseProduct'

			





