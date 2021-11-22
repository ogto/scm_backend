from jd.api.base import RestApi

class AdsDspRtbTpAddCampaignRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.putType = None
			self.billingType = None
			self.startTime = None
			self.dayBudget = None
			self.name = None
			self.endTime = None
			self.campaignType = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.addCampaign'

			





