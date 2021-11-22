from app.main.stores.jd.api.base import RestApi

class AdsDspRtbFeaturedCampaignListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.pageSize = None
			self.startDay = None
			self.endDay = None
			self.clickOrOrderCaliber = None
			self.impressionOrClickEffect = None
			self.campaignType = None
			self.orderStatusCategory = None
			self.status = None
			self.nameLike = None
			self.name = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.campaignList'

			





