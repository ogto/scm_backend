from app.main.stores.jd.api.base import RestApi

class AscAuditRefuseRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
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
			self.operateRemark = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.audit.refuse'

			





