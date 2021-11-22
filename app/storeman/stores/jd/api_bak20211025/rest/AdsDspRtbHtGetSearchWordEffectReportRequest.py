from app.main.stores.jd.api.base import RestApi

class AdsDspRtbHtGetSearchWordEffectReportRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.isDaily = None
			self.startDay = None
			self.endDay = None
			self.obys = None
			self.clickOrOrderDay = None
			self.clickOrOrderCaliber = None
			self.province = None
			self.filters = None
			self.page = None
			self.pageSize = None
			self.platform = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.ht.getSearchWordEffectReport'

			





