from jd.api.base import RestApi

class UeInsuranceSearchInsuranceOrdersRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.pageSize = None
			self.page = None

		def getapiname(self):
			return 'jingdong.ue.insurance.searchInsuranceOrders'

			





