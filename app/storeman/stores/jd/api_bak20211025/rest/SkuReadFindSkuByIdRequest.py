from app.storeman.stores.jd.api.base import RestApi

class SkuReadFindSkuByIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.field = None

		def getapiname(self):
			return 'jingdong.sku.read.findSkuById'

			





