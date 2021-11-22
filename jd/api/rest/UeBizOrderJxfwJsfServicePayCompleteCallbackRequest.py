from jd.api.base import RestApi

class UeBizOrderJxfwJsfServicePayCompleteCallbackRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.receivedAmt = None
			self.orderNo = None
			self.appId = None
			self.operateDate = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.payCompleteCallback'

			





