from jd.api.base import RestApi

class AscProcessListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.expressCode = None
			self.applyTimeBegin = None
			self.applyTimeEnd = None
			self.serviceStatus = None
			self.customerExpect = None
			self.approveTimeBegin = None
			self.approveTimeEnd = None
			self.jdInterveneFlag = None
			self.customerPin = None
			self.timeoutFlag = None
			self.skuId = None
			self.pageNumber = None
			self.pageSize = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.process.list'

			





