from jd.api.base import RestApi

class PriceWriteUpdateWareCostPriceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.costPrice = None

		def getapiname(self):
			return 'jingdong.price.write.updateWareCostPrice'

			





