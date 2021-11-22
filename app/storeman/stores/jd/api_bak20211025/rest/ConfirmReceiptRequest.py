from app.main.stores.jd.api.base import RestApi

class ConfirmReceiptRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bizToken = None
			self.source = None
			self.projectId = None
			self.shopId = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.confirmReceipt'

			





