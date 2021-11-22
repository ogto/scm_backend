from app.main.stores.jd.api.base import RestApi

class UeRecoveryOrderGetRecyclerSettleBillDetailRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.code = None
			self.page = None
			self.pageSize = None
			self.settleNo = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.getRecyclerSettleBillDetail'

			





