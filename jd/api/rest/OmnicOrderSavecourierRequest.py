from jd.api.base import RestApi

class OmnicOrderSavecourierRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.orderId = None
			self.deliveryId = None
			self.carrierType = None
			self.carrierName = None
			self.carrierNo = None

		def getapiname(self):
			return 'jingdong.omnic.order.savecourier'

			





