from app.main.stores.jd.api.base import RestApi

class JosMasterKeyGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sig = None
			self.sdk_ver = None
			self.ts = None
			self.tid = None

		def getapiname(self):
			return 'jingdong.jos.master.key.get'

			





