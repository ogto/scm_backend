from jd.api.base import RestApi

class LogisticsPoGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.inbound_no = None

		def getapiname(self):
			return 'jingdong.logistics.po.get'

			





