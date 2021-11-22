from app.main.stores.jd.api.base import RestApi

class LdopAbnormalGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customerCode = None

		def getapiname(self):
			return 'jingdong.ldop.abnormal.get'

			





