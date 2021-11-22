from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceRepairServiceCompleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.createBy = None
			self.orderNo = None
			self.appId = None
			self.dealResult = None
			self.operateDate = None
			self.dealRemark = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.repairServiceComplete'

			





