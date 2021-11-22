from app.main.stores.jd.api.base import RestApi

class JpassJournalQueryRefundBillRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bid = None
			self.businessBillId = None
			self.orderId = None
			self.refOrderId = None
			self.storeId = None
			self.refStoreId = None
			self.sId = None
			self.happenTime = None
			self.happenTimeBegin = None
			self.happenTimeEnd = None
			self.settleStatus = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.jpass.journal.queryRefundBill'

			





