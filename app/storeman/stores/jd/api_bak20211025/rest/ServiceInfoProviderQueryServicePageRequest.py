from app.main.stores.jd.api.base import RestApi

class ServiceInfoProviderQueryServicePageRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None
			self.buId = None
			self.orderId = None
			self.afsApplyTimeBegin = None
			self.afsApplyTimeEnd = None
			self.afsServiceStep = None
			self.afsServiceProcessResult = None
			self.approvedDateBegin = None
			self.approvedDateEnd = None
			self.customerPin = None
			self.customerName = None
			self.customerTel = None
			self.orderType = None
			self.pageSize = None
			self.pageIndex = None
			self.operatorPin = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None
			self.platformSrc = None
			self.expressCode = None
			self.newOrderId = None
			self.verificationCode = None

		def getapiname(self):
			return 'jingdong.ServiceInfoProvider.queryServicePage'

			





