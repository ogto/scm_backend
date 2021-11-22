from jd.api.base import RestApi

class AdsDspRtbTpAdListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignType = None
			self.billingType = None
			self.clickOrOrderDay = None
			self.clickOrOrderCaliber = None
			self.giftFlag = None
			self.orderStatusCategory = None
			self.startDay = None
			self.endDay = None
			self.status = None
			self.nameLike = None
			self.campaignId = None
			self.groupId = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.adList'

			





