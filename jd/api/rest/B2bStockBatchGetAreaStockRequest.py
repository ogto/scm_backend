from jd.api.base import RestApi

class B2bStockBatchGetAreaStockRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appName = None
			self.skuId = None
			self.num = None
			self.provinceId = None
			self.cityId = None
			self.countyId = None
			self.townId = None

		def getapiname(self):
			return 'jingdong.b2b.stock.batchGetAreaStock'

			





