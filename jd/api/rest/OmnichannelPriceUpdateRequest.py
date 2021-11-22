from jd.api.base import RestApi

class OmnichannelPriceUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.saleSkuId = None
			self.saleSkuName = None
			self.outerSkuId = None
			self.outerSkuName = None
			self.upc = None
			self.outerStoreId = None
			self.priceMode = None
			self.price = None
			self.updateTime = None

		def getapiname(self):
			return 'jingdong.omnichannel.price.update'

			





