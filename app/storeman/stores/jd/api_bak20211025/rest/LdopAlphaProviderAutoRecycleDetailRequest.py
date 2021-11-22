from app.main.stores.jd.api.base import RestApi

class LdopAlphaProviderAutoRecycleDetailRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.providerCode = None
			self.startTime = None
			self.endTime = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.ldop.alpha.provider.autoRecycleDetail'

			





