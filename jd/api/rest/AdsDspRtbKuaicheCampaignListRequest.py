from jd.api.base import RestApi

class AdsDspRtbKuaicheCampaignListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.putType = None
			self.pageSize = None
			self.clickOrOrderDay = None
			self.campaignType = None
			self.giftFlag = None
			self.campaignId = None
			self.orderStatusCategory = None
			self.status = None
			self.endDay = None
			self.nameLike = None
			self.activityId = None
			self.startDay = None
			self.page = None
			self.platform = None
			self.clickOrOrderCaliber = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.campaign.list'

			





