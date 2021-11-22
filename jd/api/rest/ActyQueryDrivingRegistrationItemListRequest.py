from jd.api.base import RestApi

class ActyQueryDrivingRegistrationItemListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.orderId = None
			self.beginDate = None
			self.endDate = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.acty.queryDrivingRegistrationItemList'

			





