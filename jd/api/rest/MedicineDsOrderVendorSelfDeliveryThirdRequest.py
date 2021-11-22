from jd.api.base import RestApi

class MedicineDsOrderVendorSelfDeliveryThirdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.deliveryPhone = None
			self.operatePerson = None
			self.deliveryPerson = None
			self.reqTimestamp = None
			self.orderId = None
			self.latitude = None
			self.storeId = None
			self.deliveryPlatform = None
			self.deliveryStatus = None
			self.longitude = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.vendorSelfDeliveryThird'

			





