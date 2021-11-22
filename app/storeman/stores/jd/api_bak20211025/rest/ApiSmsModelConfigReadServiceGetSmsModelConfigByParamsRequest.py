from app.main.stores.jd.api.base import RestApi

class ApiSmsModelConfigReadServiceGetSmsModelConfigByParamsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageNumber = None
			self.serveType = None
			self.pageSize = None
			self.businessType = None
			self.name = None

		def getapiname(self):
			return 'jingdong.storeman.SmsModelConfigReadService.getSmsModelConfigByParams'

			





