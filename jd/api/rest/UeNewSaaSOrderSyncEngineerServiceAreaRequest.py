from jd.api.base import RestApi

class UeNewSaaSOrderSyncEngineerServiceAreaRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.engineerServiceAreaIdList = None
			self.engineerId = None
			self.appId = None
			self.siteId = None

		def getapiname(self):
			return 'jingdong.ue.newSaaSOrder.syncEngineerServiceArea'

			





