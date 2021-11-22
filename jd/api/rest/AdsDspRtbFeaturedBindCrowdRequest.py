from jd.api.base import RestApi

class AdsDspRtbFeaturedBindCrowdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.crowdId = None
			self.adGroupPrice = None
			self.isUsed = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.bindCrowd'

			





