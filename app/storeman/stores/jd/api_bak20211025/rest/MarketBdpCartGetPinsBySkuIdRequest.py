from app.main.stores.jd.api.base import RestApi

class MarketBdpCartGetPinsBySkuIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.days = None

		def getapiname(self):
			return 'jingdong.market.bdp.cart.getPinsBySkuId'

			





