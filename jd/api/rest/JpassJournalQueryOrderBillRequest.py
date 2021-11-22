from jd.api.base import RestApi

class JpassJournalQueryOrderBillRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bid = None
			self.orderId = None
			self.refOrderId = None
			self.storeId = None
			self.sId = None
			self.refStoreId = None
			self.orderCompleteTime = None
			self.orderCompleteTimeBegin = None
			self.orderCompleteTimeEnd = None
			self.settleStatus = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.jpass.journal.queryOrderBill'

			





