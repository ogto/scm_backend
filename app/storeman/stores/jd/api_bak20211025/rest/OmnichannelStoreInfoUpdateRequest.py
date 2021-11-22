from app.main.stores.jd.api.base import RestApi

class OmnichannelStoreInfoUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.storeId = None
			self.storeName = None
			self.storeFullAddress = None
			self.province = None
			self.provinceCode = None
			self.city = None
			self.cityCode = None
			self.county = None
			self.countyCode = None
			self.town = None
			self.townCode = None
			self.storeContactName = None
			self.storeContactPhone = None
			self.storeContactMail = None
			self.coverage = None
			self.companyUnitCreditCode = None
			self.longitude = None
			self.latitude = None
			self.isValid = None
			self.deliveryFlag = None
			self.pickupFlag = None

		def getapiname(self):
			return 'jingdong.omnichannel.store.info.update'

			





