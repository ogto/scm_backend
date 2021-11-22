from jd.api.base import RestApi

class CmpSkuInfoQuerybyarticleidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.articleId = None

		def getapiname(self):
			return 'jingdong.cmp.sku.info.querybyarticleid'

			





