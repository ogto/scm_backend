from app.main.stores.jd.api.base import RestApi

class DeliRecomdCarriersSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.sku = None
			self.sendProvinceId = None
			self.sendCityId = None
			self.sendCountyId = None
			self.sendTownId = None
			self.receiveProvinceId = None
			self.receiveCityId = None
			self.receiveCountyId = None
			self.receiveTownId = None

		def getapiname(self):
			return 'jingdong.deliRecomdCarriers.search'

			





