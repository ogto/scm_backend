from jd.api.base import RestApi

class UeRecoveryOrderDispatchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.engineerName = None
			self.dispatch = None
			self.engineerMobile = None
			self.orderNo = None
			self.engineerIdCard = None
			self.code = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.dispatch'

			





