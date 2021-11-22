from app.main.stores.jd.api.base import RestApi

class AdsDspRtbTpAccountCampaignReportRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.campaignType = None
			self.clickOrOrderCaliber = None
			self.clickOrOrderDay = None
			self.endDay = None
			self.giftFlag = None
			self.isDaily = None
			self.page = None
			self.pageSize = None
			self.platform = None
			self.startDay = None
			self.orderStatusCategory = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.accountCampaignReport'

			





