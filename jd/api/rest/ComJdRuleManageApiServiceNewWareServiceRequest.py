from jd.api.base import RestApi

class ComJdRuleManageApiServiceNewWareServiceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.spuId = None
			self.categoryId = None
			self.brandId = None
			self.spuName = None
			self.itemNumber = None
			self.tagUrl = None

		def getapiname(self):
			return 'jingdong.com.jd.rule.manage.api.service.NewWareService'

			





