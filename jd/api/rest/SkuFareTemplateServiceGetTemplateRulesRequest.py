from jd.api.base import RestApi

class SkuFareTemplateServiceGetTemplateRulesRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.template_id = None

		def getapiname(self):
			return 'jingdong.SkuFareTemplateService.getTemplateRules'

			





