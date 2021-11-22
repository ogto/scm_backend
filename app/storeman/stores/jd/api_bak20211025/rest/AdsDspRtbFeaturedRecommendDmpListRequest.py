from app.main.stores.jd.api.base import RestApi

class AdsDspRtbFeaturedRecommendDmpListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.pageSize = None
			self.startDay = None
			self.endDay = None
			self.clickOrOrderDay = None
			self.campaignType = None
			self.campaignId = None
			self.orderStatusCategory = None
			self.impressionOrClickEffect = None
			self.clickOrOrderCaliber = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.recommendDmpList'

			





