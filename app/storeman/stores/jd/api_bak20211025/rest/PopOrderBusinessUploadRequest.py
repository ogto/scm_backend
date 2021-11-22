from app.main.stores.jd.api.base import RestApi

class PopOrderBusinessUploadRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.businessIds = None
			self.businessJson = None

		def getapiname(self):
			return 'jingdong.pop.order.business.upload'

			





