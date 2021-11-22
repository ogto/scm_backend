from jd.api.base import RestApi

class PmxPricesMgetsRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuids = None
			self.source = None
			self.area = None

		def getapiname(self):
			return 'jingdong.pmx.prices.mgets'

			





