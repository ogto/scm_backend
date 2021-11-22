from app.main.stores.jd.api.base import RestApi

class UeWateGetWaterByOrdIdAndSkuRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.sku = None

		def getapiname(self):
			return 'jingdong.ue.wate.getWaterByOrdIdAndSku'

			





