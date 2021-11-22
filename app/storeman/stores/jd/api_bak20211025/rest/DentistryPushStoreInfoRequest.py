from app.main.stores.jd.api.base import RestApi

class DentistryPushStoreInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelType = None
			self.storeName = None
			self.operateType = None
			self.status = None
			self.storeImg = None
			self.cityName = None
			self.provinceName = None
			self.storeLat = None
			self.storePhone = None
			self.storeAddr = None
			self.countyName = None
			self.storeLng = None
			self.storeId = None
			self.storeHours = None
			self.reportSupport = None

		def getapiname(self):
			return 'jingdong.dentistry.pushStoreInfo'

			





