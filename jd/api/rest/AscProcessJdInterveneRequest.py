from jd.api.base import RestApi

class AscProcessJdInterveneRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.sysVersion = None
			self.interveneReasonCid1 = None
			self.interveneReasonCid2 = None
			self.contactTel = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.process.JdIntervene'

			





