from jd.api.base import RestApi

class SwitchDeliveryModeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.storeId = None
			self.value = None

		def getapiname(self):
			return 'jingdong.switchDeliveryMode'

			





