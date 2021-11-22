from jd.api.base import RestApi

class SellerPromotionAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.name = None
			self.type = None
			self.begin_time = None
			self.end_time = None
			self.bound = None
			self.member = None
			self.slogan = None
			self.comment = None
			self.favor_mode = None

		def getapiname(self):
			return 'jingdong.seller.promotion.add'

			





