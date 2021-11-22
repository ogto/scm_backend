from app.main.stores.jd.api.base import RestApi

class AscReceiveRegisterRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.receivePin = None
			self.receiveName = None
			self.packingState = None
			self.qualityState = None
			self.invoiceRecord = None
			self.judgmentReason = None
			self.accessoryOrGift = None
			self.appearanceState = None
			self.receiveRemark = None
			self.wareNum = None

		def getapiname(self):
			return 'jingdong.asc.receive.register'

			





