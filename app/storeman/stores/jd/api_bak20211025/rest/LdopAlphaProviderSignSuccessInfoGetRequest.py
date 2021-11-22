from app.main.stores.jd.api.base import RestApi

class LdopAlphaProviderSignSuccessInfoGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderCode = None

		def getapiname(self):
			return 'jingdong.ldop.alpha.provider.sign.success.info.get'

			





