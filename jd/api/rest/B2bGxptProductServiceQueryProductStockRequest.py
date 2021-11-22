from jd.api.base import RestApi

class B2bGxptProductServiceQueryProductStockRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.skuSet = None

		def getapiname(self):
			return 'jingdong.b2b.gxpt.ProductService.queryProductStock'

			





