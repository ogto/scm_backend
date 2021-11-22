from jd.api.base import RestApi

class EdiPoStatusGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.createTimeStart = None
			self.createTimeEnd = None
			self.pageNum = None
			self.pageSize = None
			self.purchaseOrderCode = None
			self.bipLogicalDel = None
			self.bipStatus = None

		def getapiname(self):
			return 'jingdong.edi.po.status.get'

			





