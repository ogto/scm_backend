from jd.api.base import RestApi

class YunpeiPurchaseProductQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.level2_category_id = None
			self.city_name = None
			self.page_no = None
			self.page_size = None

		def getapiname(self):
			return 'jingdong.yunpei.purchase.product.query'

			





