from app.main.stores.jd.api.base import RestApi

class EclpTraceServiceJosOrderTraceByOrderServiceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.role = None
			self.userId = None

		def getapiname(self):
			return 'jingdong.eclp.trace.service.jos.OrderTraceByOrderService'

			





