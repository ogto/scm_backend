from jd.api.base import RestApi

class UeNewSaaSOrderCompanyCancelRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.createBy = None
			self.orderNo = None
			self.cancelType = None
			self.appId = None
			self.cancelReason = None

		def getapiname(self):
			return 'jingdong.ue.newSaaSOrder.companyCancel'

			





