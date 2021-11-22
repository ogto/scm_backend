from jd.api.base import RestApi

class EdiSsSendRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorName = None
			self.orderType = None
			self.purchaseOrderCode = None
			self.jdShipmentNumber = None
			self.vendorCode = None
			self.vendorShipmentNumber = None
			self.serialNumber = None
			self.sku = None
			self.vendorProductId = None

		def getapiname(self):
			return 'jingdong.edi.ss.send'

			





