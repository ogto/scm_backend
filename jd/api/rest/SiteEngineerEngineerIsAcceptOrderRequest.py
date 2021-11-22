from jd.api.base import RestApi

class SiteEngineerEngineerIsAcceptOrderRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.engineerId = None
			self.isAcceptOrder = None
			self.siteId = None

		def getapiname(self):
			return 'jingdong.siteEngineer.engineerIsAcceptOrder'

			





