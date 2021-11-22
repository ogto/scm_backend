from app.main.stores.jd.api.base import RestApi

class LogisticsStockSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.warehouse_no = None
			self.goods_no = None
			self.current_page = None

		def getapiname(self):
			return 'jingdong.logistics.stock.search'

			





