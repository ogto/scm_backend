from jd.api.base import RestApi

class PopInvoiceSelfFindRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.invoiceCode = None
			self.invoiceNo = None

		def getapiname(self):
			return 'jingdong.pop.invoice.self.find'

			





