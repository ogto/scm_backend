from app.main.stores.jd.api.base import RestApi

class SendFactoryAbutmentAssignInfoReturnRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authorizedSequence = None
			self.orderno = None
			self.assignTime = None
			self.atHomeTime = None
			self.assignerName = None
			self.assignerTel = None

		def getapiname(self):
			return 'jingdong.sendFactoryAbutmentAssignInfoReturn'

			





