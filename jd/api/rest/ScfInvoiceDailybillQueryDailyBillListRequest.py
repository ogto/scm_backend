from jd.api.base import RestApi

class ScfInvoiceDailybillQueryDailyBillListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.applyId = None
			self.rfBillType = None
			self.endDate = None
			self.beginDate = None
			self.pageNum = None

		def getapiname(self):
			return 'jingdong.scf.invoice.dailybill.queryDailyBillList'

			





