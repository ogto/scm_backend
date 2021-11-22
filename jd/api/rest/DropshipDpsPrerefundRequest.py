from jd.api.base import RestApi

class DropshipDpsPrerefundRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customOrderId = None
			self.approvalSuggestion = None
			self.approvalState = None
			self.id = None
			self.operatorState = None

		def getapiname(self):
			return 'jingdong.dropship.dps.prerefund'

			





