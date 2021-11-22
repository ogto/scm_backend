from jd.api.base import RestApi

class KuaicheZnPlanSearchKeywordUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.plan_id = None
			self.keyword_price = None

		def getapiname(self):
			return 'jingdong.kuaiche.zn.plan.search.keyword.update'

			





