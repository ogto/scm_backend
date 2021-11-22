from app.main.stores.jd.api.base import RestApi

class B2bProductGetBigFieldRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.fieldKeys = None

		def getapiname(self):
			return 'jingdong.b2b.product.getBigField'

			





