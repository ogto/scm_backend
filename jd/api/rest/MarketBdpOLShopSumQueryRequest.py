from jd.api.base import RestApi

class MarketBdpOLShopSumQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.tp = None
			self.dt = None
			self.field = None

		def getapiname(self):
			return 'jingdong.market.bdp.OLShopSum.query'

			





