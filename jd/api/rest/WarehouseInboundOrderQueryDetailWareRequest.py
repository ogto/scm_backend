from jd.api.base import RestApi

class WarehouseInboundOrderQueryDetailWareRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.docNo = None

		def getapiname(self):
			return 'jingdong.warehouse.inbound.order.query.detail.ware'

			





