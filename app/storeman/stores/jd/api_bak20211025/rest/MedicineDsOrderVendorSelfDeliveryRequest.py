from app.main.stores.jd.api.base import RestApi

class MedicineDsOrderVendorSelfDeliveryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.deliverymanPhone = None
			self.deliveryman = None
			self.operateMan = None
			self.reqTimestamp = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.vendorSelfDelivery'

			





