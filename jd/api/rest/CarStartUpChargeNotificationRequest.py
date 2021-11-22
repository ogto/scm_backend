from jd.api.base import RestApi

class CarStartUpChargeNotificationRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.StartChargeSeq = None
			self.StartChargeSeqStat = None
			self.StartTime = None
			self.IdentCode = None
			self.ConnectorID = None

		def getapiname(self):
			return 'jingdong.car.start.up.charge.notification'

			





