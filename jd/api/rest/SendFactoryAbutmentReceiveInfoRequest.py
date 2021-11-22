from jd.api.base import RestApi

class SendFactoryAbutmentReceiveInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authorizedSequence = None
			self.serviceType = None
			self.orderno = None
			self.disposeTime = None
			self.disposeResult = None
			self.remark = None

		def getapiname(self):
			return 'jingdong.sendFactoryAbutmentReceiveInfo'

			





