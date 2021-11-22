from app.main.stores.jd.api.base import RestApi

class PromotionUpdateLineationPriceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.lineationPrice = None
			self.applicant = None

		def getapiname(self):
			return 'jingdong.promotion.updateLineationPrice'

			





