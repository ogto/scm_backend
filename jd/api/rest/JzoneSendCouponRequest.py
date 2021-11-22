from jd.api.base import RestApi

class JzoneSendCouponRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channle = None
			self.deployAppName = None
			self.hostName = None
			self.clientIP = None
			self.version = None
			self.deployAppId = None
			self.activityKey = None
			self.pin = None

		def getapiname(self):
			return 'jingdong.jzone.sendCoupon'

			





