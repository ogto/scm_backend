from jd.api.base import RestApi

class OmnicStoreImportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.latitude = None
			self.storeContactName = None
			self.supplierCode = None
			self.cityId = None
			self.townId = None
			self.storeContactTelephone = None
			self.storeStatus = None
			self.mapDatum = None
			self.cityName = None
			self.scopeType = None
			self.venderStoreName = None
			self.countyId = None
			self.storeFullAddress = None
			self.closeTime = None
			self.openTime = None
			self.longitude = None
			self.countyName = None
			self.coverage = None
			self.supplierName = None
			self.townName = None
			self.provinceId = None
			self.storeContactPhone = None
			self.venderStoreId = None
			self.provinceName = None
			self.vertexs = None

		def getapiname(self):
			return 'jingdong.omnic.store.import'

			





