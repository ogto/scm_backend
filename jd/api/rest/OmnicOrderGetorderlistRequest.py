from jd.api.base import RestApi

class OmnicOrderGetorderlistRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.dateType = None
			self.orderId = None
			self.endDate = None
			self.pageSize = None
			self.currentPage = None
			self.fieldList = None
			self.startDate = None
			self.status = None

		def getapiname(self):
			return 'jingdong.omnic.order.getorderlist'

			





