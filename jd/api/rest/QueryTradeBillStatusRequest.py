from jd.api.base import RestApi

class QueryTradeBillStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.requestId = None
			self.tradeBillType = None
			self.tradeBillId = None

		def getapiname(self):
			return 'jingdong.queryTradeBillStatus'

			





