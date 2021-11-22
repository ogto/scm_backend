from jd.api.base import RestApi

class UeOrderIvcActualQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.orderId = None
			self.venderCode = None

		def getapiname(self):
			return 'jingdong.ue.order.ivcActualQuery'

			





