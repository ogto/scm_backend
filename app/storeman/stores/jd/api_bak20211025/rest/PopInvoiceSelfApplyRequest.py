from app.main.stores.jd.api.base import RestApi

class PopInvoiceSelfApplyRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.productId = None
			self.productName = None
			self.num = None
			self.price = None
			self.spec = None
			self.unit = None
			self.taxRate = None
			self.taxCategroyCode = None
			self.isTaxDiscount = None
			self.taxDiscountContent = None
			self.zeroTax = None
			self.deductions = None
			self.imei = None
			self.discount = None
			self.freight = None
			self.orderId = None
			self.receiverTaxNo = None
			self.receiverName = None
			self.invoiceCode = None
			self.invoiceNo = None
			self.ivcTitle = None
			self.totalPrice = None
			self.invoiceTime = None
			self.pdfInfo = None
			self.orderType = None
			self.ivcContentType = None
			self.ivcContentName = None
			self.eiRemark = None
			self.receiverAddress = None
			self.receiverPhone = None
			self.receiverBankName = None
			self.receiverBankAccount = None
			self.drawer = None
			self.payee = None
			self.consumerAddress = None
			self.consumerPhone = None
			self.consumerBankName = None
			self.consumerBankAccount = None

		def getapiname(self):
			return 'jingdong.pop.invoice.self.apply'

			





