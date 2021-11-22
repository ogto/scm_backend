from app.main.stores.jd.api.base import RestApi

class BrandInfoServiceQueryBrandInfoByBidRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.brandId = None

		def getapiname(self):
			return 'jingdong.BrandInfoService.queryBrandInfoByBid'

			





