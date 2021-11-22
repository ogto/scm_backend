from app.main.stores.jd.api.base import RestApi

class ScfInvoiceApplybillGetInvoiceApplyBillByVenderIdAndApplyIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.applyId = None

		def getapiname(self):
			return 'jingdong.scf.invoice.applybill.getInvoiceApplyBillByVenderIdAndApplyId'

			





