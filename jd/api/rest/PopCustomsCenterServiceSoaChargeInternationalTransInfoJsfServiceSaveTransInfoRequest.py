from jd.api.base import RestApi

class PopCustomsCenterServiceSoaChargeInternationalTransInfoJsfServiceSaveTransInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customsId = None
			self.venderId = None
			self.orderId = None
			self.platformId = None
			self.interWayBillNo = None
			self.interTransName = None
			self.interTransMode = None
			self.fromCity = None
			self.toCity = None
			self.actualW = None
			self.chargedW = None
			self.mainOrderNo = None
			self.isVolume = None
			self.tax = None
			self.ex1 = None
			self.ex2 = None
			self.ex3 = None
			self.ex4 = None
			self.ex5 = None

		def getapiname(self):
			return 'jingdong.pop.customs.center.service.soa.charge.InternationalTransInfoJsfService.saveTransInfo'

			





