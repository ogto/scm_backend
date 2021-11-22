from jd.api.base import RestApi

class MedicineDsOrderBatchUpdateStockRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.siteId = None
			self.num = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.batchUpdateStock'

			





