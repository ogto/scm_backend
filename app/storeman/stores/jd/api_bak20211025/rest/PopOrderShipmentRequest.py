from app.main.stores.jd.api.base import RestApi

class PopOrderShipmentRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.logiCoprId = None
			self.logiNo = None
			self.installId = None

		def getapiname(self):
			return 'jingdong.pop.order.shipment'

			





