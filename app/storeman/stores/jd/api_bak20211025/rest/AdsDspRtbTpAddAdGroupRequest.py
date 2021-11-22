from app.main.stores.jd.api.base import RestApi

class AdsDspRtbTpAddAdGroupRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.name = None
			self.feeDecimal = None
			self.recommendAutomatedBiddingType = None
			self.recommendTcpaBid = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.addAdGroup'

			





