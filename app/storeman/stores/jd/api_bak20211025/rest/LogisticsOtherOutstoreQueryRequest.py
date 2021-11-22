from app.main.stores.jd.api.base import RestApi

class LogisticsOtherOutstoreQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.josl_outbound_no = None

		def getapiname(self):
			return 'jingdong.logistics.otherOutstore.query'

			





