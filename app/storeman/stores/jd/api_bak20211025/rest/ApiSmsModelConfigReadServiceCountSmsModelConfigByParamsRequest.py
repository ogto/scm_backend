from app.main.stores.jd.api.base import RestApi

class ApiSmsModelConfigReadServiceCountSmsModelConfigByParamsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.serveType = None
			self.name = None
			self.businessType = None

		def getapiname(self):
			return 'jingdong.storeman.SmsModelConfigReadService.countSmsModelConfigByParams'

			





