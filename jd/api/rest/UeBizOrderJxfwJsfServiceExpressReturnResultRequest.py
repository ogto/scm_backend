from jd.api.base import RestApi

class UeBizOrderJxfwJsfServiceExpressReturnResultRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.appId = None
			self.remark = None
			self.operateDate = None
			self.deliveredResult = None

		def getapiname(self):
			return 'jingdong.ue.bizOrderJxfwJsfService.expressReturnResult'

			





