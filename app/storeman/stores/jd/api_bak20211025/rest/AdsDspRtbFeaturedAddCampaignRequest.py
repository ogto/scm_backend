from app.main.stores.jd.api.base import RestApi

class AdsDspRtbFeaturedAddCampaignRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startTime = None
			self.endTime = None
			self.dayBudget = None
			self.campaignType = None
			self.name = None
			self.uniformSpeed = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.addCampaign'

			





