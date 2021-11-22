from app.main.stores.jd.api.base import RestApi

class CmpSkuInfoQuerylistRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuIds = None

		def getapiname(self):
			return 'jingdong.cmp.sku.info.querylist'

			





