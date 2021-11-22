from app.main.stores.jd.api.base import RestApi

class AfsserviceServicelogGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None
			self.pageNumber = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.afsservice.servicelog.get'

			





