from app.main.stores.jd.api.base import RestApi

class WarehouseOutboundOrderQueryConditionRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageIndex = None
			self.pageSize = None
			self.stockOutNo = None
			self.createTimeBegin = None
			self.createTimeEnd = None

		def getapiname(self):
			return 'jingdong.warehouse.outbound.order.query.condition'

			





