from jd.api.base import RestApi

class GetSkuUpdateSettlePriceInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.venderCode = None

		def getapiname(self):
			return 'jingdong.getSkuUpdateSettlePriceInfo'

			





