from jd.api.base import RestApi

class MedicineDsOrderGetOrderOpRecRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.clientIp = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.getOrderOpRec'

			





