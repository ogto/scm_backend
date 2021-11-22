from jd.api.base import RestApi

class LdopCenterApiReceivePaymentInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.deliveryId = None
			self.customerCode = None
			self.recMoney = None
			self.receivedMoney = None
			self.paymentState = None
			self.paymentTime = None
			self.payer = None

		def getapiname(self):
			return 'jingdong.ldop.center.api.receivePaymentInfo'

			





