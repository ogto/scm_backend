from jd.api.base import RestApi

class UeRecoveryOrderGetRecyclerSettleBillStatRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.code = None
			self.settleNo = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.getRecyclerSettleBillStat'

			





