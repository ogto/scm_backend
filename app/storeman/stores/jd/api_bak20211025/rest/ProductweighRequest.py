from app.main.stores.jd.api.base import RestApi

class ProductweighRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.oneOrderId = None
			self.skuId = None
			self.actualWeight = None
			self.billingWeight = None
			self.jysSkuLength = None
			self.jysSkuWidth = None
			self.jysSkuHeight = None
			self.extStr = None

		def getapiname(self):
			return 'jingdong.productweigh'

			





