from app.main.stores.jd.api.base import RestApi

class EclpCoQueryLwbByConditionRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.deptNo = None

		def getapiname(self):
			return 'jingdong.eclp.co.queryLwbByCondition'

			





