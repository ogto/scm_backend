from app.main.stores.jd.api.base import RestApi

class VcAplsStockBatchGetProdStockInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorCode = None
			self.skuList = None

		def getapiname(self):
			return 'jingdong.vc.apls.stock.batchGetProdStockInfo'

			





