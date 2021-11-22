from app.main.stores.jd.api.base import RestApi

class AdsDspRtbTpBatchUpdateCampaignStatusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignIds = None
			self.status = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.batchUpdateCampaignStatus'

			





