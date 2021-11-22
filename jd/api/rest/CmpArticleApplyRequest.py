from jd.api.base import RestApi

class CmpArticleApplyRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.remark = None
			self.applyType = None

		def getapiname(self):
			return 'jingdong.cmp.article.apply'

			





