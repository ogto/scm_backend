from app.main.stores.jd.api.base import RestApi

class FactoryProductQueryProductByPageRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.personalKey = None
			self.ptId = None
			self.startTime = None
			self.endTime = None
			self.materialType = None
			self.subType = None
			self.skuList = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.factory.product.queryProductByPage'

			





