from app.main.stores.jd.api.base import RestApi

class GetVenderStoreInfoListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.exStoreId = None
			self.pageIndex = None
			self.pageSize = None
			self.storeId = None
			self.storeName = None
			self.storeStatus = None
			self.firstAddress = None
			self.secondAddress = None
			self.thirdAddress = None

		def getapiname(self):
			return 'jingdong.getVenderStoreInfoList'

			





