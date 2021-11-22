from jd.api.base import RestApi

class CarStopChargeNotificationRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.StartChargeSeq = None
			self.SuccStat = None
			self.StartChargeSeqStat = None
			self.FailReason = None
			self.ConnectorID = None

		def getapiname(self):
			return 'jingdong.car.stop.charge.notification'

			





