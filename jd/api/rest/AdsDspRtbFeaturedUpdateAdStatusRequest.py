from jd.api.base import RestApi

class AdsDspRtbFeaturedUpdateAdStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operateType = None
			self.ids = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.updateAdStatus'

			





