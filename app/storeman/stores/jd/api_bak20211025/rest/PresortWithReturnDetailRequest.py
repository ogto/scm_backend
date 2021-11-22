from app.main.stores.jd.api.base import RestApi

class PresortWithReturnDetailRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.batchId = None
			self.responseCode = None
			self.responseMessage = None
			self.provinceId = None
			self.cityId = None
			self.countyId = None
			self.townId = None
			self.fullAddress = None
			self.companyCode = None
			self.waybillCode = None
			self.phoneCode = None
			self.provinceName = None
			self.cityName = None
			self.countyName = None
			self.townName = None
			self.lat = None
			self.lng = None

		def getapiname(self):
			return 'jingdong.presortWithReturnDetail'

			





