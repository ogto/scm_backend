from app.main.stores.jd.api.base import RestApi

class PopMarketReadInnerGetPromotionByRfidRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ip = None
			self.requestId = None
			self.port = None
			self.rfId = None

		def getapiname(self):
			return 'jingdong.pop.market.read.inner.getPromotionByRfid'

			





