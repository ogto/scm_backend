from jd.api.base import RestApi

class DentistryPushReportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.reportStr = None
			self.channelType = None
			self.appiontmentNo = None
			self.jdAppointmentId = None

		def getapiname(self):
			return 'jingdong.dentistry.pushReport'

			





