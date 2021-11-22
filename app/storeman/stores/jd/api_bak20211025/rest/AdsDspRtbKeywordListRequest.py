from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKeywordListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.putType = None
			self.pageSize = None
			self.clickOrOrderDay = None
			self.giftFlag = None
			self.campaignId = None
			self.endDay = None
			self.groupId = None
			self.startDay = None
			self.page = None
			self.platform = None
			self.clickOrOrderCaliber = None
			self.orderStatusCategory = None
			self.nameLike = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.keyword.list'

			





