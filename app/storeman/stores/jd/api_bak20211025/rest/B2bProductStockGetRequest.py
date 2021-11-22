from app.main.stores.jd.api.base import RestApi

class B2bProductStockGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuNums = None
			self.area = None

		def getapiname(self):
			return 'jingdong.b2b.product.stock.get'

			





