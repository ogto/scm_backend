from jd.api.base import RestApi

class AnSspPositionreportserviceListtagIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.pageNo = None
			self.pageSize = None
			self.endDate = None

		def getapiname(self):
			return 'jingdong.an.ssp.positionreportservice.listtagId'

			





