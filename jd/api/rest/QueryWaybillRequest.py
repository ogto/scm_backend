from jd.api.base import RestApi

class QueryWaybillRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.projectId = None
			self.shopId = None
			self.orderList = None
			self.orderType = None
			self.bizToken = None
			self.source = None

		def getapiname(self):
			return 'jingdong.queryWaybill'

			





