from jd.api.base import RestApi

class AscAuditFetchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.fetchNum = None

		def getapiname(self):
			return 'jingdong.asc.audit.fetch'

			





