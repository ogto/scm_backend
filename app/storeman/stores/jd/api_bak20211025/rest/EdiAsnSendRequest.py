from app.main.stores.jd.api.base import RestApi

class EdiAsnSendRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.purchaseOrderCode = None
			self.deliveryCenterCode = None
			self.deliveryCenterName = None
			self.warehouseCode = None
			self.warehouseName = None
			self.vendorName = None
			self.vendorShipmentCode = None
			self.jdShipmentCode = None
			self.deleted = None
			self.supposedShipmentTime = None
			self.supposedArrivedTime = None
			self.vendorCode = None
			self.jdSku = None
			self.vendorProductId = None
			self.productName = None
			self.quantity = None

		def getapiname(self):
			return 'jingdong.edi.asn.send'

			





