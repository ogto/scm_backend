from app.main.stores.jd.api.base import RestApi

class PopMarketWritePromotionSumDeleteSkusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ip = None
			self.port = None
			self.request_id = None
			self.rfId = None
			self.promoId = None
			self.skuId = None
			self.operator1 = None

		def getapiname(self):
			return 'jingdong.pop.market.write.promotion.sum.deleteSkus'

			





