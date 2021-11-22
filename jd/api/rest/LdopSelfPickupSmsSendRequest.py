from jd.api.base import RestApi

class LdopSelfPickupSmsSendRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waybillCode = None
			self.customerCode = None

		def getapiname(self):
			return 'jingdong.ldop.self.pickup.sms.send'

			





