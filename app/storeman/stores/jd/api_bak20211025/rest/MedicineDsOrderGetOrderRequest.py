from app.main.stores.jd.api.base import RestApi

class MedicineDsOrderGetOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.clientIp = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.getOrder'

			





