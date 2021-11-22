from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceInformationManufacturerReturnedRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.appId = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.informationManufacturerReturned'

			





