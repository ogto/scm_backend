from jd.api.base import RestApi

class CustomerserviceDataQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.searchType = None
			self.startTime = None
			self.endTime = None
			self.groupId = None
			self.dimension = None
			self.queryType = None

		def getapiname(self):
			return 'jingdong.customerservice.data.query'

			





