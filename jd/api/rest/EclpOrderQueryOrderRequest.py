from jd.api.base import RestApi

class EclpOrderQueryOrderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.eclpSoNo = None

		def getapiname(self):
			return 'jingdong.eclp.order.queryOrder'

			





