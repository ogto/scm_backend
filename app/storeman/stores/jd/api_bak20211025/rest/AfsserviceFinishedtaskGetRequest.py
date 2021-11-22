from app.main.stores.jd.api.base import RestApi

class AfsserviceFinishedtaskGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None
			self.pageNumber = None
			self.pageSize = None
			self.customerPin = None
			self.orderId = None
			self.afsApplyTimeBegin = None
			self.afsApplyTimeEnd = None

		def getapiname(self):
			return 'jingdong.afsservice.finishedtask.get'

			





