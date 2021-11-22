from app.main.stores.jd.api.base import RestApi

class SkuWriteMergeSkuFeaturesRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.featureKey = None
			self.featureValue = None

		def getapiname(self):
			return 'jingdong.sku.write.mergeSkuFeatures'

			





