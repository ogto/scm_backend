from jd.api.base import RestApi

class SvcBookingVerificationInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.verificationCode = None
			self.lcnNo = None
			self.appId = None

		def getapiname(self):
			return 'jingdong.svc.booking.verification.info'

			





