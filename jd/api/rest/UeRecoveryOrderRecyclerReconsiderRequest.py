from jd.api.base import RestApi

class UeRecoveryOrderRecyclerReconsiderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.code = None
			self.settleNo = None
			self.dealRemark = None
			self.dealType = None
			self.invoiceNo = None
			self.createBy = None

		def getapiname(self):
			return 'jingdong.ue.recovery.order.recyclerReconsider'

			





