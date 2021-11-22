from app.main.stores.jd.api.base import RestApi

class HealthcarePushStoreInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.storeAddr = None
			self.storeName = None
			self.storeId = None
			self.storeType = None
			self.storePhone = None
			self.channelType = None
			self.status = None
			self.reportSupport = None
			self.storeLevel = None
			self.storeLat = None
			self.storeLng = None
			self.provinceName = None
			self.cityName = None
			self.countyName = None
			self.operateType = None
			self.storeHours = None

		def getapiname(self):
			return 'jingdong.healthcare.pushStoreInfo'

			





