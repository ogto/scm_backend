from jd.api.base import RestApi

class AdsDspRtbKuaicheCampaignUpdatebudgetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.dateRange = None
			self.id = None
			self.dayBudget = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.campaign.updatebudget'

			





