from jd.api.base import RestApi

class AscSyncListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.serviceStatus = None
			self.orderType = None
			self.updateTimeBegin = None
			self.updateTimeEnd = None
			self.freightUpdateDateBegin = None
			self.freightUpdateDateEnd = None
			self.pageNumber = None
			self.pageSize = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.sync.list'

			





