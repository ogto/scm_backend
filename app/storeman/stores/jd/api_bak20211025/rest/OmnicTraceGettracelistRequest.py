from app.main.stores.jd.api.base import RestApi

class OmnicTraceGettracelistRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.dateType = None
			self.statusType = None
			self.orderId = None
			self.endDate = None
			self.pageSize = None
			self.currentPage = None
			self.startDate = None
			self.status = None

		def getapiname(self):
			return 'jingdong.omnic.trace.gettracelist'

			





