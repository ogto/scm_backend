from app.main.stores.jd.api.base import RestApi

class DlzMerchantOrderTraceCallbackJsfServiceServiceCallbackRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customsId = None
			self.serviceId = None
			self.orderId = None
			self.platformId = None
			self.methodType = None
			self.operateType = None
			self.operateTime = None

		def getapiname(self):
			return 'jingdong.DlzMerchantOrderTraceCallbackJsfService.serviceCallback'

			





