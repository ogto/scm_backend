from jd.api.base import RestApi

class B2bOrderLogisticsGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.jdOrderId = None

		def getapiname(self):
			return 'jingdong.b2b.order.logistics.get'

			





