from app.main.stores.jd.api.base import RestApi

class MedicineDsOrderConfirmAcceptOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.operateMan = None
			self.reqTimestamp = None
			self.agreed = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.confirmAcceptOrder'

			





