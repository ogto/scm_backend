from jd.api.base import RestApi

class UeRecoveryOrderBookedRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.engineerFinalOperate = None
			self.userFinalOnsite = None
			self.userFirstOnsite = None
			self.engineerFirstOperate = None
			self.orderNo = None
			self.code = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.booked'

			





