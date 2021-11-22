from jd.api.base import RestApi

class UeRecoveryOrderTakeOutRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.data = None
			self.code = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.takeOut'

			





