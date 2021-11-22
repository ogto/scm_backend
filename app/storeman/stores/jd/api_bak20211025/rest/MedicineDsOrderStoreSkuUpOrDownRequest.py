from app.main.stores.jd.api.base import RestApi

class MedicineDsOrderStoreSkuUpOrDownRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.exStoreId = None
			self.skuId = None
			self.storeSkuStatus = None
			self.storeId = None
			self.outerId = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.storeSkuUpOrDown'

			





