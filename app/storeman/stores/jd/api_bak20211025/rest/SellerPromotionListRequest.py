from app.main.stores.jd.api.base import RestApi

class SellerPromotionListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.type = None
			self.status = None
			self.begin_time = None
			self.end_time = None
			self.sku_id = None
			self.favor_mode = None
			self.page = None
			self.size = None

		def getapiname(self):
			return 'jingdong.seller.promotion.list'

			





