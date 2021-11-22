from app.main.stores.jd.api.base import RestApi

class ApiSmsModelConfigWriteServiceSendSmsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.orderId = None
			self.pin = None
			self.batchNo = None
			self.phoneNo = None
			self.open_id_buyer = None

		def getapiname(self):
			return 'jingdong.storeman.SmsModelConfigWriteService.sendSms'

			





