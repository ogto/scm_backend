from jd.api.base import RestApi

class AdsDspRtbTpAccountUserReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
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
			return 'jingdong.ads.dsp.rtb.tp.accountUserReport'

			





