from app.main.stores.jd.api.base import RestApi

class EclpStockQueryAdventGoodsStockRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.deptNo = None
			self.warehouseNos = None
			self.goodsNos = None
			self.currentPage = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.eclp.stock.queryAdventGoodsStock'

			





