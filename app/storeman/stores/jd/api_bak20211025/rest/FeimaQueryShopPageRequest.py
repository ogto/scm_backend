from app.main.stores.jd.api.base import RestApi

class FeimaQueryShopPageRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.projectId = None
			self.shopId = None
			self.index = None
			self.bizToken = None
			self.source = None

		def getapiname(self):
			return 'jingdong.feima.queryShopPage'

			





