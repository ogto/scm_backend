from app.main.stores.jd.api.base import RestApi

class B2bWareDetailGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelEnum = None
			self.bSkuGetExtendEnumsKyes = None
			self.bSkuGetEnumsKeys = None
			self.jdSkuIdsKeys = None

		def getapiname(self):
			return 'jingdong.b2b.ware.detail.get'

			





