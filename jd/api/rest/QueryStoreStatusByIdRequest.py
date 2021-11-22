from jd.api.base import RestApi

class QueryStoreStatusByIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.storeId = None

		def getapiname(self):
			return 'jingdong.queryStoreStatusById'

			





