from jd.api.base import RestApi

class AdsDspRtbKuaicheCampaignUpdatedateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startTime = None
			self.id = None
			self.endTime = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.campaign.updatedate'

			





