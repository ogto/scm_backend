from app.main.stores.jd.api.base import RestApi

class LasImHfsReservationPushRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderid = None
			self.appointmentstatus = None
			self.appointmenttimebegin = None
			self.appointmenttimeend = None
			self.serviceproviderno = None
			self.operator = None
			self.operatetime = None
			self.ordertype = None

		def getapiname(self):
			return 'jingdong.las.im.hfs.reservation.push'

			





