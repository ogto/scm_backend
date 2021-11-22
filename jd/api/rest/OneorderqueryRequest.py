from jd.api.base import RestApi

class OneorderqueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.endDate = None
			self.orderStatus = None
			self.page = None
			self.pageSize = None
			self.sortType = None
			self.dateType = None
			self.operationType = None
			self.extStr = None

		def getapiname(self):
			return 'jingdong.oneorderquery'

			





