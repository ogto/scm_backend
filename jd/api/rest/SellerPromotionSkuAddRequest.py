from jd.api.base import RestApi

class SellerPromotionSkuAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promo_id = None
			self.sku_ids = None
			self.jd_prices = None
			self.promo_prices = None
			self.seq = None
			self.num = None
			self.bind_type = None

		def getapiname(self):
			return 'jingdong.seller.promotion.sku.add'

			





