from app.main.stores.jd.api.base import RestApi

class CancelAsmsServiceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.serviceId = None
			self.operatorName = None
			self.operatorPin = None
			self.cancelReason = None
			self.venderCode = None

		def getapiname(self):
			return 'jingdong.cancelAsmsService'

			





