from jd.api.base import RestApi

class LogisticsSkuAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bar_code = None
			self.sku_id = None
			self.name = None
			self.goods_abbreviation = None
			self.category_id = None
			self.category_name = None
			self.brand_no = None
			self.brand_name = None
			self.format = None
			self.color = None
			self.size = None
			self.gross_weight = None
			self.net_weight = None
			self.size_definition = None
			self.suppliers_name = None
			self.manufacturer = None
			self.suppliers_no = None
			self.product_area = None
			self.length = None
			self.width = None
			self.height = None
			self.volume = None
			self.is_safe = None
			self.safe_date = None

		def getapiname(self):
			return 'jingdong.logistics.sku.add'

			





