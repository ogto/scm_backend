from app.main.stores.jd.api.base import RestApi

class B2bGxptServiceErpServiceQueryServiceListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.applyStartDate = None
			self.purchaseId = None
			self.orderStatus = None
			self.pageSize = None
			self.applyEndDate = None
			self.type = None
			self.submitEndDate = None
			self.pageIndex = None
			self.serviceStatus = None
			self.submitStartDate = None
			self.serviceId = None
			self.saleServiceType = None
			self.startModified = None
			self.endModified = None

		def getapiname(self):
			return 'jingdong.b2b.gxpt.serviceErpService.queryServiceList'

			





