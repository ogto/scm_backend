from jd.api.base import RestApi

class UeInsuranceUpdateStateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.extensionEndDate = None
			self.orderNo = None
			self.handleType = None
			self.extensionBeginDate = None
			self.agreementNo = None
			self.failCause = None
			self.appId = None

		def getapiname(self):
			return 'jingdong.ue.insurance.updateState'

			





