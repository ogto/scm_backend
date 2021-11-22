from jd.api.base import RestApi

class EdiStatementQueryStatementRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.billNo = None

		def getapiname(self):
			return 'jingdong.edi.statement.queryStatement'

			





