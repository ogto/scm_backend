from jd.api.base import RestApi

class SendFactoryAbutmentDistributeInfoReturnRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authorizedSequence = None
			self.orderno = None
			self.distributeTime = None
			self.distributeOutletsName = None
			self.distributeOutletsPhone = None

		def getapiname(self):
			return 'jingdong.sendFactoryAbutmentDistributeInfoReturn'

			





