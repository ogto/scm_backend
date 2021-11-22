from jd.api.base import RestApi

class SellerPromotionV2UnitLimitCreateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ip = None
			self.port = None
			self.request_id = None
			self.promo_name = None
			self.begin_time = None
			self.end_time = None
			self.slogan = None
			self.comment = None
			self.link = None
			self.allow_others_operate = None
			self.allow_others_check = None
			self.allow_other_user_operate = None
			self.allow_other_user_check = None
			self.need_manual_check = None
			self.freq_bound = None
			self.per_max_num = None
			self.per_min_num = None
			self.promo_area_type = None
			self.promo_areas = None
			self.sku_id = None
			self.promo_price = None
			self.limit_num = None

		def getapiname(self):
			return 'jingdong.seller.promotion.v2.unit.limit.create'

			





