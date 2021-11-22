from jd.api.base import RestApi

class JiliRefundPaymentResultSyncRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.tenantId = None
			self.detailId = None
			self.payChannel = None
			self.confirmTime = None
			self.type = None
			self.resMsg = None
			self.status = None
			self.receiptId = None
			self.accountSn = None

		def getapiname(self):
			return 'jingdong.jili.refund.payment.result.sync'

			





