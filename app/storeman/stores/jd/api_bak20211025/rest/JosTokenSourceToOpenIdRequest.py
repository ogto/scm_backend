from app.main.stores.jd.api.base import RestApi

class JosTokenSourceToOpenIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.token = None
			self.source = None
			self.appKey = None

		def getapiname(self):
			return 'jingdong.jos.token.source.to.openId'

			





