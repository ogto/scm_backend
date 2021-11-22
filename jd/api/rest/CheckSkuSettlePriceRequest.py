from jd.api.base import RestApi

class CheckSkuSettlePriceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.rejectedReason = None
			self.id = None
			self.sku = None
			self.checkStat = None
			self.venderCode = None
			self.appid = None

		def getapiname(self):
			return 'jingdong.checkSkuSettlePrice'

			





