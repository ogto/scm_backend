from app.main.stores.jd.api.base import RestApi

class HealthcareAppointmentResultCallbackRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.msg = None
			self.code = None
			self.reportId = None
			self.jdAppointmentId = None
			self.resultDate = None
			self.channelType = None
			self.appointmentNo = None
			self.resultType = None

		def getapiname(self):
			return 'jingdong.healthcare.appointmentResultCallback'

			





