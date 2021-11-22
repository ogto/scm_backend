from jd.api.base import RestApi

class QuerySymbolApprovalListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.approvalStatus = None
			self.pageSize = None
			self.searchKey = None
			self.bdsBindTypeEnum = None
			self.pageNo = None
			self.symbolName = None

		def getapiname(self):
			return 'jingdong.querySymbolApprovalList'

			





