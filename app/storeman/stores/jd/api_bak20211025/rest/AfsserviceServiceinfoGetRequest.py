from app.main.stores.jd.api.base import RestApi

class AfsserviceServiceinfoGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None

		def getapiname(self):
			return 'jingdong.afsservice.serviceinfo.get'

			





