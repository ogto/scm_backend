from jd.api.base import RestApi

class AfsserviceReceivetaskGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
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
			return 'jingdong.afsservice.receivetask.get'

			





