from app.main.stores.jd.api.base import RestApi

class B2bGxptPurchaseOrderErpServiceFindErpOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.purchaseOrderId = None
			self.jdOrderId = None

		def getapiname(self):
			return 'jingdong.b2b.gxpt.purchaseOrderErpService.findErpOrder'

			





