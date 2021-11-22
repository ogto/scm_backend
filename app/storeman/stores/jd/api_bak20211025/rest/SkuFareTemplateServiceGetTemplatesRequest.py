from app.storeman.stores.jd.api.base import RestApi

class SkuFareTemplateServiceGetTemplatesRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)

		def getapiname(self):
			return 'jingdong.SkuFareTemplateService.getTemplates'

			





