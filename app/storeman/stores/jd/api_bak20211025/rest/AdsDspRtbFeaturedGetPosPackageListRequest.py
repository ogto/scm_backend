from app.main.stores.jd.api.base import RestApi

class AdsDspRtbFeaturedGetPosPackageListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignType = None
			self.device = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.getPosPackageList'

			





