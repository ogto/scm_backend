from jd.api.base import RestApi

class SellerPromotionSamclubAreaCreateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.app_secret = None
			self.ip = None
			self.host_name = None
			self.deploy_app_name = None
			self.deploy_app_id = None
			self.requestId = None
			self.sku_id = None
			self.normal_price = None
			self.club_price = None
			self.areas = None

		def getapiname(self):
			return 'jingdong.seller.promotion.samclub.area.create'

			





