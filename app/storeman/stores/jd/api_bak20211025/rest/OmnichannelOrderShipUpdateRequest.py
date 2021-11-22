from app.main.stores.jd.api.base import RestApi

class OmnichannelOrderShipUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.deliveryId = None
			self.status = None
			self.operateName = None
			self.contactPhone = None
			self.operateTime = None

		def getapiname(self):
			return 'jingdong.omnichannel.order.ship.update'

			





