from app.main.stores.jd.api.base import RestApi

class PopCustomsCenterServiceCallbackJsfServiceServiceCallbackRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.serviceId = None
			self.customsId = None
			self.orderStatus = None
			self.orderDesc = None
			self.goodsCheck = None

		def getapiname(self):
			return 'jingdong.pop.customs.center.ServiceCallbackJsfService.serviceCallback'

			





