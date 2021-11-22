from jd.api.base import RestApi

class SamOrderInfoQuerynewRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderStatus = None
			self.payStartTime = None
			self.payEndTime = None
			self.startTime = None
			self.endTime = None
			self.pageNum = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.sam.order.info.querynew'

			





