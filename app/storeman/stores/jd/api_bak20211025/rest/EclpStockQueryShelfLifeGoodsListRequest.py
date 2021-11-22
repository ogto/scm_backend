from app.main.stores.jd.api.base import RestApi

class EclpStockQueryShelfLifeGoodsListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.deptNo = None
			self.warehouseNo = None
			self.goodsNo = None
			self.isvGoodsNo = None
			self.status = None
			self.goodsLevel = None
			self.currentPage = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.eclp.stock.queryShelfLifeGoodsList'

			





