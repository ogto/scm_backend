from app.main.stores.jd.api.base import RestApi

class PurchaseOrderGetInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.purchaseId = None

		def getapiname(self):
			return 'jingdong.purchase.order.get.info'

			





