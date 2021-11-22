from jd.api.base import RestApi

class QueryProdInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.shopId = None
			self.projectId = None
			self.skuList = None
			self.isProduct = None
			self.bizToken = None
			self.source = None

		def getapiname(self):
			return 'jingdong.queryProdInfo'

			





