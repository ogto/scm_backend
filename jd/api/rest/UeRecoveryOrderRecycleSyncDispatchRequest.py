from jd.api.base import RestApi

class UeRecoveryOrderRecycleSyncDispatchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.code = None
			self.appid = None
			self.orderNo = None
			self.engineerIdCard = None
			self.engineerName = None
			self.engineerMobile = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.recycleSyncDispatch'

			





