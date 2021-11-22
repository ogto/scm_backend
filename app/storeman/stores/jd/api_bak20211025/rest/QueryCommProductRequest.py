from app.main.stores.jd.api.base import RestApi

class QueryCommProductRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
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
			return 'jingdong.queryCommProduct'

			





