from jd.api.base import RestApi

class SubmitRefundRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.freightFeeFlag = None
			self.vendorPin = None
			self.afsServiceId = None
			self.vendorCode = None
			self.businessUnit = None

		def getapiname(self):
			return 'jingdong.submitRefund'

			





