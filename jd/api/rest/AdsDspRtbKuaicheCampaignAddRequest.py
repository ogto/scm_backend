from jd.api.base import RestApi

class AdsDspRtbKuaicheCampaignAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.putType = None
			self.startTime = None
			self.dayBudget = None
			self.campaignType = None
			self.name = None
			self.endTime = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.campaign.add'

			





