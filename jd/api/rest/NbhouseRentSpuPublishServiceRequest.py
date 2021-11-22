from jd.api.base import RestApi

class NbhouseRentSpuPublishServiceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.staffId = None
			self.plotId = None
			self.spuId = None
			self.spuName = None
			self.skuId = None
			self.skuName = None
			self.houseSourceCode = None

		def getapiname(self):
			return 'jingdong.nbhouse.rent.spu.publishService'

			





