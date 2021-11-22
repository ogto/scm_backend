from jd.api.base import RestApi

class SvcBindNumberRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.id = None

		def getapiname(self):
			return 'jingdong.svc.bind.number'

			





