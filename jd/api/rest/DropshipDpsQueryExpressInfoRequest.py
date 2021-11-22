from jd.api.base import RestApi

class DropshipDpsQueryExpressInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customOrderIds = None

		def getapiname(self):
			return 'jingdong.dropship.dps.queryExpressInfo'

			





