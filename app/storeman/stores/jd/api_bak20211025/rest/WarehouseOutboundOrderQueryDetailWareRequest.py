from app.main.stores.jd.api.base import RestApi

class WarehouseOutboundOrderQueryDetailWareRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.stockOutNo = None

		def getapiname(self):
			return 'jingdong.warehouse.outbound.order.query.detail.ware'

			





