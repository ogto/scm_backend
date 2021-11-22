from jd.api.base import RestApi

class AdsDspRtbKuaicheCampaignDeleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ids = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.campaign.delete'

			





