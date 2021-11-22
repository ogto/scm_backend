from jd.api.base import RestApi

class WaitAuditApplysProviderFindWaitAuditApplysRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None
			self.orderId = None
			self.customerPin = None
			self.customerName = None
			self.customerTel = None
			self.orderType = None
			self.afsApplyTimeBegin = None
			self.afsApplyTimeEnd = None
			self.customerExpect = None
			self.afsServiceStatus = None
			self.buId = None
			self.pageSize = None
			self.pageIndex = None
			self.operatorPin = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None
			self.platformSrc = None
			self.verificationCode = None
			self.queryTabName = None
			self.afsServiceState = None

		def getapiname(self):
			return 'jingdong.WaitAuditApplysProvider.findWaitAuditApplys'

			





