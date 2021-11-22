from app.main.stores.jd.api.base import RestApi

class DropshipDpsBatchOutBoundRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customOrderId = None
			self.memoByVendor = None
			self.isJdexpress = None
			self.parentOrderId = None
			self.addressId = None

		def getapiname(self):
			return 'jingdong.dropship.dps.batchOutBound'

			





