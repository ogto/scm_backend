from jd.api.base import RestApi

class MarketBdpSaleVenderSkuRankQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.opTime = None
			self.tp = None
			self.field = None

		def getapiname(self):
			return 'jingdong.market.bdp.saleVenderSkuRank.query'

			





