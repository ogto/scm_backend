from app.main.stores.jd.api.base import RestApi

class OmnicOrderTraceSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.statusType = None
			self.status = None
			self.currentPage = None
			self.pageSize = None
			self.startDate = None
			self.endDate = None
			self.dateType = None

		def getapiname(self):
			return 'jingdong.omnic.order.trace.search'

			





