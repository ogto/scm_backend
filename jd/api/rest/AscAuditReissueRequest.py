from jd.api.base import RestApi

class AscAuditReissueRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.approveNotes = None
			self.sysVersion = None
			self.approveReasonCid1 = None
			self.approveReasonCid2 = None
			self.expressCode = None
			self.shipWayId = None
			self.shipWayName = None
			self.operateRemark = None
			self.extJsonStr = None
			self.wareNum = None

		def getapiname(self):
			return 'jingdong.asc.audit.reissue'

			





