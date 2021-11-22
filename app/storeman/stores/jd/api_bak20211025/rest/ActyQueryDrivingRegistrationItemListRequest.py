from app.main.stores.jd.api.base import RestApi

class ActyQueryDrivingRegistrationItemListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
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

			





