from jd.api.base import RestApi

class UeNewSaaSOrderGetChangeOrderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.ivs = None

		def getapiname(self):
			return 'jingdong.ue.newSaaSOrder.getChangeOrder'

			





