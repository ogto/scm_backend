from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKuaicheAccountAdGroupReportRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageSize = None
			self.clickOrOrderDay = None
			self.giftFlag = None
			self.orderStatusCategory = None
			self.endDay = None
			self.isDaily = None
			self.startDay = None
			self.page = None
			self.platform = None
			self.clickOrOrderCaliber = None
			self.campaignId = None
			self.deliveryType = None
			self.groupId = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.accountAdGroupReport'

			





