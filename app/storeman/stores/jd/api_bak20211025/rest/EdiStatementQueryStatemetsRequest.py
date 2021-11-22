from app.main.stores.jd.api.base import RestApi

class EdiStatementQueryStatemetsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startTime = None
			self.endTime = None
			self.vendorCode = None

		def getapiname(self):
			return 'jingdong.edi.statement.queryStatemets'

			





