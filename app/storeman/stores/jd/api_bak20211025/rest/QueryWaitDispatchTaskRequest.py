from app.main.stores.jd.api.base import RestApi

class QueryWaitDispatchTaskRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.serviceState = None
			self.pageSize = None
			self.pageIndex = None
			self.venderCode = None

		def getapiname(self):
			return 'jingdong.queryWaitDispatchTask'

			





