from jd.api.base import RestApi

class AdsDspRtbKuaicheAccountKeywordReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startDay = None
			self.endDay = None
			self.platform = None
			self.clickOrOrderDay = None
			self.clickOrOrderCaliber = None
			self.giftFlag = None
			self.orderStatusCategory = None
			self.campaignId = None
			self.groupId = None
			self.isDaily = None
			self.targetingType = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.accountKeywordReport'

			





