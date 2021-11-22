from jd.api.base import RestApi

class PopCustomsCenterServiceSoaDlzClearanceCustomClearanceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customsId = None
			self.serviceId = None
			self.orderId = None
			self.platformId = None
			self.result = None
			self.message = None
			self.goodsCheck = None

		def getapiname(self):
			return 'jingdong.pop.customs.center.service.soa.dlz.clearance.customClearance'

			





