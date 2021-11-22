from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceManufacturerOrderStateUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.appId = None
			self.takeMan = None
			self.deliverNo = None
			self.remark = None
			self.deliverCompany = None
			self.type = None
			self.takeDate = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.manufacturerOrderStateUpdate'

			





