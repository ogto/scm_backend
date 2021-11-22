from jd.api.base import RestApi

class JiliTcsOfflineRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.tenantId = None
			self.storeId = None
			self.pin = None
			self.pinType = None

		def getapiname(self):
			return 'jingdong.jili.tcs.offline'

			





