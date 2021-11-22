from app.main.stores.jd.api.base import RestApi

class PopInvoiceSelfRedRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.invoiceCode = None
			self.invoiceNo = None
			self.invoiceTime = None
			self.blueInvoiceCode = None
			self.blueInvoiceNo = None
			self.pdfInfo = None

		def getapiname(self):
			return 'jingdong.pop.invoice.self.red'

			





