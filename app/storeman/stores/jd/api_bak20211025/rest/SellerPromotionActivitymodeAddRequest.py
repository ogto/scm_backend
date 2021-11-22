from app.main.stores.jd.api.base import RestApi

class SellerPromotionActivitymodeAddRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promo_id = None
			self.num_bound = None
			self.freq_bound = None
			self.per_max_num = None
			self.per_min_num = None

		def getapiname(self):
			return 'jingdong.seller.promotion.activitymode.add'

			





