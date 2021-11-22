from jd.api.base import RestApi

class AscApplyViewRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operateNick = None
			self.serviceId = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.asc.apply.view'

			





