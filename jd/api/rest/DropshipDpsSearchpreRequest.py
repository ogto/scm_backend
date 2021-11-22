from jd.api.base import RestApi

class DropshipDpsSearchpreRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageSize = None
			self.page = None
			self.beginDate = None
			self.endDate = None

		def getapiname(self):
			return 'jingdong.dropship.dps.searchpre'

			





