from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKeywordBootRecommendListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.keyWord = None
			self.adGroupId = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.keyword.boot.recommend.list'

			





