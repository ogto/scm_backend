from jd.api.base import RestApi

class ServicecallbackMerchantOrderTraceCallbackJsfServiceServiceCallbackRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customsId = None
			self.serviceId = None
			self.orderId = None
			self.methodType = None
			self.operateType = None
			self.operateTime = None

		def getapiname(self):
			return 'jingdong.servicecallback.MerchantOrderTraceCallbackJsfService.serviceCallback'

			





