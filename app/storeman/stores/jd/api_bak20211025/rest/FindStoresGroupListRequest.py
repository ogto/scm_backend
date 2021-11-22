from app.main.stores.jd.api.base import RestApi

class FindStoresGroupListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.name = None
			self.groupId = None
			self.type = None
			self.businessId = None
			self.brandId = None
			self.creator = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.findStoresGroupList'

			





