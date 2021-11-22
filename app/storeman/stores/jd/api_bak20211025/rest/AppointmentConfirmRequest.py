from app.main.stores.jd.api.base import RestApi

class AppointmentConfirmRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderCode = None
			self.asmsServiceId = None
			self.engineer = None
			self.engineerName = None
			self.appointmentTime = None

		def getapiname(self):
			return 'jingdong.appointmentConfirm'

			





