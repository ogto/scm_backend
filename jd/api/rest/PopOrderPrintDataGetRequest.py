from jd.api.base import RestApi

class PopOrderPrintDataGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_id = None

		def getapiname(self):
			return 'jingdong.pop.order.print.data.get'

			





