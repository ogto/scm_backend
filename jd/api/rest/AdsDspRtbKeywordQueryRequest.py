from jd.api.base import RestApi

class AdsDspRtbKeywordQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.groupId = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.keyword.query'

			





