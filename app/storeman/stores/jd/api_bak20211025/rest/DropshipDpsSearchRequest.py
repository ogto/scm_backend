from app.main.stores.jd.api.base import RestApi

class DropshipDpsSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageSize = None
			self.page = None
			self.beginDate = None
			self.endDate = None

		def getapiname(self):
			return 'jingdong.dropship.dps.search'

			





