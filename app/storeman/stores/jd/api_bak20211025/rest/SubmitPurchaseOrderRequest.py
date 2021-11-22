from app.main.stores.jd.api.base import RestApi

class SubmitPurchaseOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.source = None
			self.projectId = None
			self.shopId = None
			self.paymentId = None
			self.totalPrice = None
			self.bizToken = None
			self.skuId = None
			self.skuNum = None
			self.purchasePrice = None

		def getapiname(self):
			return 'jingdong.submitPurchaseOrder'

			





