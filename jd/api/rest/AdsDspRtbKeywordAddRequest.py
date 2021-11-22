from jd.api.base import RestApi

class AdsDspRtbKeywordAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.groupId = None
			self.keywordName = None
			self.keywordPrice = None
			self.type = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.keyword.add'

			





