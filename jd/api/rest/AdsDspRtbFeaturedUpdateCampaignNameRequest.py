from jd.api.base import RestApi

class AdsDspRtbFeaturedUpdateCampaignNameRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.name = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.updateCampaignName'

			





