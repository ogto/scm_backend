from app.main.stores.jd.api.base import RestApi

class PopMarketRetrievePromotionGetPromotionListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ip = None
			self.request_id = None
			self.port = None
			self.promoStatus = None
			self.skuId = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.pop.market.retrieve.promotion.getPromotionList'

			





