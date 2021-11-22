from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceManufacturerOrderDispatchInformationRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.appId = None
			self.deliverNo = None
			self.deliverCompany = None
			self.type = None
			self.operateDate = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.manufacturerOrderDispatchInformation'

			





