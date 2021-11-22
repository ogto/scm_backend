from jd.api.base import RestApi

class AdsDspRtbFeaturedEffectHisMediaOrderQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.pageSize = None
			self.startDay = None
			self.endDay = None
			self.orderStatusCategory = None
			self.impressionOrClickEffect = None
			self.platform = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.effectHisMediaOrderQuery'

			





