from jd.api.base import RestApi

class EdiStatementQueryInvoiceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.invoiceNo = None

		def getapiname(self):
			return 'jingdong.edi.statement.queryInvoice'

			





