from app.main.stores.jd.api.base import RestApi

class SellerPromotionGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promo_id = None

		def getapiname(self):
			return 'jingdong.seller.promotion.get'

			





