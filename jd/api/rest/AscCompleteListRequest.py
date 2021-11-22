from jd.api.base import RestApi

class AscCompleteListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.processResult = None
			self.verificationCode = None
			self.orderType = None
			self.customerPin = None
			self.expressCode = None
			self.pageNumber = None
			self.pageSize = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.complete.list'

			





