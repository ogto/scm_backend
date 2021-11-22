from app.main.stores.jd.api.base import RestApi

class UpdateEntityStoresGroupRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.name = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.updateEntityStoresGroup'

			





