from jd.api.base import RestApi

class CarNotificationStationStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.ConnectorID = None
			self.Status = None
			self.ParkStatus = None
			self.LockStatus = None

		def getapiname(self):
			return 'jingdong.car.notificationStationStatus'

			





