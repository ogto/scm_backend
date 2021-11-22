from jd.api.base import RestApi

class EclpTraceServiceJosCommonTraceServiceQueryTraceByOrderIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.source = None
			self.sign = None
			self.t = None

		def getapiname(self):
			return 'jingdong.eclp.trace.service.jos.CommonTraceService.queryTraceByOrderId'

			





