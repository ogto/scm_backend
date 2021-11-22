from app.main.stores.jd.api.base import RestApi

class SellerPromotionOrdermodeAddRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promo_id = None
			self.favor_mode = None
			self.quota = None
			self.rate = None
			self.plus = None
			self.minus = None
			self.link = None
			self.free_postage = None

		def getapiname(self):
			return 'jingdong.seller.promotion.ordermode.add'

			





