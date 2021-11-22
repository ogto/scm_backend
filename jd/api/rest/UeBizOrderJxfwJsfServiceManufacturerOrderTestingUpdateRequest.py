from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceManufacturerOrderTestingUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.createBy = None
			self.orderNo = None
			self.expectPrice = None
			self.appId = None
			self.checkReportUrl = None
			self.checkMan = None
			self.checkDate = None
			self.operateDate = None
			self.checkResult = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.manufacturerOrderTestingUpdate'

			





