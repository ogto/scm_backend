from app.main.stores.jd.api.base import RestApi

class MedicineDsOrderGetStorePriceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.outerId = None
			self.exStoreId = None
			self.storeId = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.getStorePrice'

			





