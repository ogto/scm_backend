from jd.api.base import RestApi

class DspSoaDmpQuerySearchCrowdListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.groupId = None
			self.campaignId = None
			self.campaignType = None
			self.startDay = None
			self.endDay = None
			self.clickOrOrderCaliber = None
			self.clickOrOrderDay = None
			self.orderStatusCategory = None
			self.impressionOrClickEffect = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.soa.dmp.querySearchCrowdList'

			





