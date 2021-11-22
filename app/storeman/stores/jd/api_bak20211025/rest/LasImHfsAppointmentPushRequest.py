from app.main.stores.jd.api.base import RestApi

class LasImHfsAppointmentPushRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ord_no = None
			self.ser_pro_no = None
			self.ope_t = None
			self.ser_det = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.appointment.push'

			





