from app.main.stores.jd.api.base import RestApi

class TemplateReadFindTemplateByIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.templateId = None
			self.field = None

		def getapiname(self):
			return 'jingdong.template.read.findTemplateById'

			





