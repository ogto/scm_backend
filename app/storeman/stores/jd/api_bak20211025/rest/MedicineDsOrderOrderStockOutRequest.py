from app.main.stores.jd.api.base import RestApi

class MedicineDsOrderOrderStockOutRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.carrierName = None
			self.orderId = None
			self.waybillCode = None
			self.operateMan = None
			self.carrierId = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.orderStockOut'

			





