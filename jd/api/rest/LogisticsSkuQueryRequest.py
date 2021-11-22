from jd.api.base import RestApi

class LogisticsSkuQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.josl_good_no = None
			self.isv_good_no = None

		def getapiname(self):
			return 'jingdong.logistics.sku.query'

			





