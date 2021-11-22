from app.main.stores.jd.api.base import RestApi

class UeOrderConfirmBizProgressRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.orderNos = None
			self.type = None

		def getapiname(self):
			return 'jingdong.ue.order.confirmBizProgress'

			





