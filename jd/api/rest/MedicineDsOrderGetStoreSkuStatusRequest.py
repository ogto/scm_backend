from jd.api.base import RestApi

class MedicineDsOrderGetStoreSkuStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.exStoreId = None
			self.skuId = None
			self.storeId = None
			self.outerId = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.getStoreSkuStatus'

			





