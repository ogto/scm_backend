from jd.api.base import RestApi

class OpenpresortRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.fullAddress = None
			self.companyCode = None
			self.waybillCode = None

		def getapiname(self):
			return 'jingdong.openpresort'

			





