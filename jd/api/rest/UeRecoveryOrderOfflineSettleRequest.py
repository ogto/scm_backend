from jd.api.base import RestApi

class UeRecoveryOrderOfflineSettleRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.code = None
			self.orderNo = None
			self.secondPic = None
			self.settle = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.offlineSettle'

			





