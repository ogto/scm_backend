from jd.api.base import RestApi

class DropshipDpsOutboundRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customOrderId = None
			self.memoByVendor = None
			self.isJdexpress = None
			self.addressId = None

		def getapiname(self):
			return 'jingdong.dropship.dps.outbound'

			





