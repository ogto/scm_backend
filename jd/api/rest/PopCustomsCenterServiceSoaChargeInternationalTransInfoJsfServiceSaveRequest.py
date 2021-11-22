from jd.api.base import RestApi

class PopCustomsCenterServiceSoaChargeInternationalTransInfoJsfServiceSaveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customsId = None
			self.serviceId = None
			self.orderId = None
			self.platformId = None
			self.interWayBillNo = None
			self.interTransName = None
			self.interTransMode = None
			self.fromCity = None
			self.toCity = None
			self.actualW = None
			self.chargedW = None

		def getapiname(self):
			return 'jingdong.pop.customs.center.service.soa.charge.InternationalTransInfoJsfService.save'

			





