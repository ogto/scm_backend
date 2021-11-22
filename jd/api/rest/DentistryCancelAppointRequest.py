from jd.api.base import RestApi

class DentistryCancelAppointRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelType = None
			self.jdAppointmentId = None
			self.appointmentNo = None
			self.remark = None

		def getapiname(self):
			return 'jingdong.dentistry.cancelAppoint'

			





