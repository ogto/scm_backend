from jd.api.base import RestApi

class LasImHfsOrderSearchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.code = None
			self.offset = None
			self.no = None
			self.token = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.order.search'

			





