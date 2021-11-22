from jd.api.base import RestApi

class AscProcessOfflineChangeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.operateRemark = None
			self.serviceId = None
			self.orderId = None
			self.sysVersion = None
			self.opFlag = None
			self.partExpressId = None
			self.shipWayId = None
			self.shipWayName = None
			self.expressCode = None
			self.relationBillId = None
			self.wareType = None
			self.partSrc = None
			self.extJsonStr = None
			self.wareNum = None

		def getapiname(self):
			return 'jingdong.asc.process.offline.change'

			





