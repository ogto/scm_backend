from app.main.stores.jd.api.base import RestApi

class QueryPurchaseOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.projectId = None
			self.shopId = None
			self.beginTime = None
			self.endTime = None
			self.completedBeginTime = None
			self.completedEndTime = None
			self.index = None
			self.pageSize = None
			self.bizToken = None
			self.source = None
			self.orderList = None

		def getapiname(self):
			return 'jingdong.queryPurchaseOrder'

			





