from jd.api.base import RestApi

class StoreQueryStoreHouseRentlistRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.page_size = None

		def getapiname(self):
			return 'jingdong.store.queryStoreHouseRentlist'

			





