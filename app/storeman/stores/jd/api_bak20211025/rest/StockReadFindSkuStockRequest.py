from app.main.stores.jd.api.base import RestApi

class StockReadFindSkuStockRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.field = None

		def getapiname(self):
			return 'jingdong.stock.read.findSkuStock'

			





