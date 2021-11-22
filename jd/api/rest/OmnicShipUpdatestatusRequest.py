from jd.api.base import RestApi

class OmnicShipUpdatestatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.deliveryId = None
			self.orderId = None
			self.operateTime = None
			self.operateName = None
			self.contactPhone = None
			self.status = None

		def getapiname(self):
			return 'jingdong.omnic.ship.updatestatus'

			





