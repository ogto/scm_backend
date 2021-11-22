from jd.api.base import RestApi

class OneorderiteminvalidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.oneOrderId = None
			self.skuId = None
			self.refuseType = None
			self.refuseReason = None
			self.extStr = None

		def getapiname(self):
			return 'jingdong.oneorderiteminvalid'

			





