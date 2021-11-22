from app.main.stores.jd.api.base import RestApi

class OmnicOrderSyncpickupcodeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.pickUpCode = None
			self.salesChannelOrderId = None

		def getapiname(self):
			return 'jingdong.omnic.order.syncpickupcode'

			





