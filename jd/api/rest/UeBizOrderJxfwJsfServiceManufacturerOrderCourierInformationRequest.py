from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceManufacturerOrderCourierInformationRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.expressmanCode = None
			self.orderNo = None
			self.expressmanMobile = None
			self.appId = None
			self.remark = None
			self.expressmanName = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.manufacturerOrderCourierInformation'

			





