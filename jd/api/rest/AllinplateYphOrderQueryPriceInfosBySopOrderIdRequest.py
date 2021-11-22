from jd.api.base import RestApi

class AllinplateYphOrderQueryPriceInfosBySopOrderIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.systermName = None
			self.queryCondition = None
			self.extendStr = None

		def getapiname(self):
			return 'jingdong.allinplate.yphOrder.queryPriceInfosBySopOrderId'

			





