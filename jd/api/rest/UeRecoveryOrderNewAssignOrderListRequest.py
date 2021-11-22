from jd.api.base import RestApi

class UeRecoveryOrderNewAssignOrderListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.code = None
			self.appid = None
			self.data = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.newAssignOrderList'

			





