from jd.api.base import RestApi

class PurchaseOrderStockOutRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.purchaseId = None
			self.shipmentId = None
			self.shipmentNo = None
			self.tradeNo = None

		def getapiname(self):
			return 'jingdong.purchase.order.stock.out'

			





