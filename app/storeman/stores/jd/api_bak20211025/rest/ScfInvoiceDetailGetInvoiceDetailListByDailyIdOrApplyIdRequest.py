from app.main.stores.jd.api.base import RestApi

class ScfInvoiceDetailGetInvoiceDetailListByDailyIdOrApplyIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.applyId = None
			self.dailyId = None
			self.pageNum = None

		def getapiname(self):
			return 'jingdong.scf.invoice.detail.getInvoiceDetailListByDailyIdOrApplyId'

			





