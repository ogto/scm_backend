from jd.api.base import RestApi

class UeNewSaaSOrderSearchOrderDeliverListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.beginDate = None
			self.orderNo = None
			self.endDate = None
			self.appId = None
			self.pageSize = None
			self.page = None

		def getapiname(self):
			return 'jingdong.ue.newSaaSOrder.searchOrderDeliverList'

			





