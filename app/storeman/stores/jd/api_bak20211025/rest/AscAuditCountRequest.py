from app.main.stores.jd.api.base import RestApi

class AscAuditCountRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.customerExpect = None
			self.serviceStatus = None
			self.timeoutFlag = None
			self.orderId = None
			self.orderType = None
			self.skuId = None
			self.customerPin = None
			self.customerName = None
			self.customerTel = None
			self.verificationCode = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.audit.count'

			





