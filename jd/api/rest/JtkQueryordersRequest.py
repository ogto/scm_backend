from jd.api.base import RestApi

class JtkQueryordersRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.endDate = None
			self.pageIndex = None
			self.pageSize = None
			self.startDate = None

		def getapiname(self):
			return 'jingdong.jtk.queryorders'

			





