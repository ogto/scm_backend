from app.main.stores.jd.api.base import RestApi

class DentistryUpdateAppointRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.goodsId = None
			self.channelType = None
			self.appointEndTime = None
			self.appointBeginTime = None
			self.jdAppointmentId = None
			self.appointmentNo = None
			self.storeId = None
			self.appointDate = None

		def getapiname(self):
			return 'jingdong.dentistry.updateAppoint'

			





