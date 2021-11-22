from jd.api.base import RestApi

class DentistryAppointmentResultCallbackRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelType = None
			self.resultType = None
			self.jdAppointmentId = None
			self.code = None
			self.resultDate = None
			self.appointmentNo = None
			self.msg = None

		def getapiname(self):
			return 'jingdong.dentistry.appointmentResultCallback'

			





