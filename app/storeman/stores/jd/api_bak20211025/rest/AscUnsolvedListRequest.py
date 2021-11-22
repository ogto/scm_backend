from app.main.stores.jd.api.base import RestApi

class AscUnsolvedListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.jdInterveneFlag = None
			self.applyTimeBegin = None
			self.applyTimeEnd = None
			self.verificationCode = None
			self.expressCode = None
			self.orderType = None
			self.customerPin = None
			self.processResult = None
			self.messageStatus = None
			self.pageNumber = None
			self.pageSize = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.unsolved.list'

			





