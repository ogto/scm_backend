from jd.api.base import RestApi

class AscServiceAndRefundViewRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.applyTimeBegin = None
			self.applyTimeEnd = None
			self.approveTimeBegin = None
			self.approveTimeEnd = None
			self.pageNumber = None
			self.pageSize = None
			self.extJsonStr = None
			self.buId = None

		def getapiname(self):
			return 'jingdong.asc.serviceAndRefund.view'

			





