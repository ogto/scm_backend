from jd.api.base import RestApi

class DropshipDpsDeliveryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customOrderId = None
			self.carrierId = None
			self.carrierBusinessName = None
			self.shipNo = None
			self.estimateDate = None
			self.carrierPhone = None

		def getapiname(self):
			return 'jingdong.dropship.dps.delivery'

			





