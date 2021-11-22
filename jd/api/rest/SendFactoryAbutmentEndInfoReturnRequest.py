from jd.api.base import RestApi

class SendFactoryAbutmentEndInfoReturnRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authorizedSequence = None
			self.orderno = None
			self.serviceEndState = None
			self.serviceEndStateLevelTow = None
			self.serviceEndStateLevelTowDescribe = None
			self.serviceEndTime = None
			self.cancelRemark = None

		def getapiname(self):
			return 'jingdong.sendFactoryAbutmentEndInfoReturn'

			





