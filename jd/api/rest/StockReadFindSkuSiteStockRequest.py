from jd.api.base import RestApi

class StockReadFindSkuSiteStockRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.siteId = None
			self.venderSource = None
			self.stockNum = None
			self.orderBookingNum = None
			self.appBookingNum = None
			self.canUsedNum = None

		def getapiname(self):
			return 'jingdong.stock.read.findSkuSiteStock'

			





