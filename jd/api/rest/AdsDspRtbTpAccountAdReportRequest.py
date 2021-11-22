from jd.api.base import RestApi

class AdsDspRtbTpAccountAdReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.campaignType = None
			self.groupId = None
			self.adId = None
			self.clickOrOrderCaliber = None
			self.clickOrOrderDay = None
			self.endDay = None
			self.giftFlag = None
			self.isDaily = None
			self.page = None
			self.pageSize = None
			self.startDay = None
			self.orderStatusCategory = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.accountAdReport'

			





