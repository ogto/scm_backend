from jd.api.base import RestApi

class AdsDspRtbFeaturedUpdateAdGroupPriceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.fee = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.updateAdGroupPrice'

			





