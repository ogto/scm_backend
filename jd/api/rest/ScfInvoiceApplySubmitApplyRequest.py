from jd.api.base import RestApi

class ScfInvoiceApplySubmitApplyRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.invoiceDirection = None
			self.invoiceOrg = None
			self.pin = None
			self.venderId = None
			self.rfBillType = None
			self.dailyBillId = None

		def getapiname(self):
			return 'jingdong.scf.invoice.apply.submitApply'

			





