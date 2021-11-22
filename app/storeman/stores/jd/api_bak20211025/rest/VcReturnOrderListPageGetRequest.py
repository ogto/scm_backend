from app.main.stores.jd.api.base import RestApi

class VcReturnOrderListPageGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.returnId = None
			self.fromDeliverCenterId = None
			self.returnStates = None
			self.createDateBegin = None
			self.createDateEnd = None
			self.pageSize = None
			self.pageIndex = None

		def getapiname(self):
			return 'jingdong.vc.return.order.list.page.get'

			





