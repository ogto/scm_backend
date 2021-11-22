from app.main.stores.jd.api.base import RestApi

class PopInvoiceSelfQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.invoiceCode = None
			self.invoiceNo = None
			self.invoiceType = None
			self.invoiceTimeStart = None
			self.invoiceTimeEnd = None
			self.pageSize = None
			self.pageCurrent = None

		def getapiname(self):
			return 'jingdong.pop.invoice.self.query'

			





