from jd.api.base import RestApi

class AdsDspRtbGetAccountListReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.isDaily = None
			self.startDay = None
			self.endDay = None
			self.obys = None
			self.clickOrOrderDay = None
			self.clickOrOrderCaliber = None
			self.orderStatusCategory = None
			self.page = None
			self.pageSize = None
			self.filters = None
			self.giftFlag = None
			self.platform = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.getAccountListReport'

			





