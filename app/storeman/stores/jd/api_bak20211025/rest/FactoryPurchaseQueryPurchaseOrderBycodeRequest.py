from app.main.stores.jd.api.base import RestApi

class FactoryPurchaseQueryPurchaseOrderBycodeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.factoryId = None
			self.personalKey = None
			self.ptId = None
			self.code = None

		def getapiname(self):
			return 'jingdong.factory.purchase.queryPurchaseOrderBycode'

			





