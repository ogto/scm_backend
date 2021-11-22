from jd.api.base import RestApi

class EdiPoaSendRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorCode = None
			self.vendorName = None
			self.purchaseOrderCode = None
			self.recordCount = None
			self.categoryNumber = None
			self.totalNubmer = None
			self.totalAmount = None
			self.actualTotalAmount = None
			self.purchaseDate = None
			self.arrivalDate = None
			self.purchaseContact = None
			self.receivingAddress = None
			self.comments = None
			self.currentRecordCount = None
			self.linePurchaseOrderCode = None
			self.productCode = None
			self.buyerProductId = None
			self.vendorSku = None
			self.productName = None
			self.quantity = None
			self.orderQuantity = None
			self.salePrice = None
			self.listPrice = None
			self.discountRate = None
			self.backOrderProcessing = None
			self.lineComments = None

		def getapiname(self):
			return 'jingdong.edi.poa.send'

			





