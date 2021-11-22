from jd.api.base import RestApi

class PopOrderBusinessUploadRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.businessIds = None
			self.businessJson = None

		def getapiname(self):
			return 'jingdong.pop.order.business.upload'

			





