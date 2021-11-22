from jd.api.base import RestApi

class JiliOrderCompleteSyncOrderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.tenantId = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.jili.order.complete.syncOrder'

			





