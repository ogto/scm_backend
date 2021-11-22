from app.main.stores.jd.api.base import RestApi

class EdiSdvCustomerEvaluationSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sku = None
			self.score = None
			self.sortType = None
			self.page = None
			self.pageSize = None
			self.pin = None

		def getapiname(self):
			return 'jingdong.edi.sdv.customer.evaluation.search'

			





