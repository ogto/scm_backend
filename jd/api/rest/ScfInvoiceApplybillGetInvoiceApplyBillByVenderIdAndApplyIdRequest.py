from jd.api.base import RestApi

class ScfInvoiceApplybillGetInvoiceApplyBillByVenderIdAndApplyIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.applyId = None

		def getapiname(self):
			return 'jingdong.scf.invoice.applybill.getInvoiceApplyBillByVenderIdAndApplyId'

			





