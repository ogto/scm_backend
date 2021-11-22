from app.main.stores.jd.api.base import RestApi

class LasSpareZerostockServiceSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.begin = None
			self.end = None
			self.index = None
			self.vc = None
			self.token = None

		def getapiname(self):
			return 'jingdong.las.spare.zerostock.service.search'

			





