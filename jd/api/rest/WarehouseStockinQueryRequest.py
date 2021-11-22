from jd.api.base import RestApi

class WarehouseStockinQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageIndex = None

		def getapiname(self):
			return 'jingdong.warehouse.stockin.query'

			





