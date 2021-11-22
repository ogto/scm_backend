from jd.api.base import RestApi

class AdsDspRtbKuaicheDmpBindRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adGroupPrice = None
			self.crowdId = None
			self.isUsed = None
			self.adGroupId = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.dmp.bind'

			





