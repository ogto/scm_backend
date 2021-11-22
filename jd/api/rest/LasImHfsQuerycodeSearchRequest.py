from jd.api.base import RestApi

class LasImHfsQuerycodeSearchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.no = None
			self.token = None
			self.date = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.querycode.search'

			





