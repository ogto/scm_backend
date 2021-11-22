from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKeywordSkuRecommendListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.skuId = None
			self.devType = None
			self.adKeywordTypes = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.keyword.sku.recommend.list'

			





