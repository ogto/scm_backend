from jd.api.base import RestApi

class UeOrderSettleCheckBizProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operateDate = None
			self.appId = None
			self.orderNo = None
			self.createBy = None
			self.settleCode = None

		def getapiname(self):
			return 'jingdong.ue.order.settleCheckBizProgress'

			





