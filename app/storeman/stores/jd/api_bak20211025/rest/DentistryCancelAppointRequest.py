from app.main.stores.jd.api.base import RestApi

class DentistryCancelAppointRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelType = None
			self.jdAppointmentId = None
			self.appointmentNo = None
			self.remark = None

		def getapiname(self):
			return 'jingdong.dentistry.cancelAppoint'

			





