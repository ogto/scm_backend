from jd.api.base import RestApi

class OmnicStockImportRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.jdSkuId = None
			self.stockType = None
			self.outerSkuId = None
			self.upc = None
			self.updateTime = None
			self.spotStockNum = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.omnic.stock.import'

			





