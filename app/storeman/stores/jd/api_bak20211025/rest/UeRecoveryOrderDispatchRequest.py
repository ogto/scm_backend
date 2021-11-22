from app.main.stores.jd.api.base import RestApi

class UeRecoveryOrderDispatchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.engineerName = None
			self.dispatch = None
			self.engineerMobile = None
			self.orderNo = None
			self.code = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.dispatch'

			





