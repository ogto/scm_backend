from app.main.stores.jd.api.base import RestApi

class PriceWriteUpdateWareMarketPriceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.marketPrice = None

		def getapiname(self):
			return 'jingdong.price.write.updateWareMarketPrice'

			





