from app.main.stores.jd.api.base import RestApi

class EclpStockQueryBatchAttrStockRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cursor = None
			self.stockType = None
			self.goodsLevel = None
			self.pageSize = None
			self.startTime = None
			self.page = None
			self.endTime = None
			self.sku = None
			self.deptNo = None
			self.warehouseNo = None
			self.isvGoodsNos = None

		def getapiname(self):
			return 'jingdong.eclp.stock.queryBatchAttrStock'

			





