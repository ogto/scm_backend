from app.main.stores.jd.api.base import RestApi

class LogisticsOtherInstoreQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.in_bound_no = None

		def getapiname(self):
			return 'jingdong.logistics.otherInstore.query'

			





