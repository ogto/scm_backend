from jd.api.base import RestApi

class AuditRefuseProviderAuditRefuseRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.serviceId = None
			self.approveNotes = None
			self.operatorPin = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None
			self.platformSrc = None

		def getapiname(self):
			return 'jingdong.AuditRefuseProvider.auditRefuse'

			





