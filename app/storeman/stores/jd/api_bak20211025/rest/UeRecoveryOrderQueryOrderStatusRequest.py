from app.main.stores.jd.api.base import RestApi

class UeRecoveryOrderQueryOrderStatusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.code = None
			self.appid = None
			self.data = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.queryOrderStatus'

			





