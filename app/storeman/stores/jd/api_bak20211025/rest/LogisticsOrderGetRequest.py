from app.main.stores.jd.api.base import RestApi

class LogisticsOrderGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.receipt_no = None

		def getapiname(self):
			return 'jingdong.logistics.order.get'

			





