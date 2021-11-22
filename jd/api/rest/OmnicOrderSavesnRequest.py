from jd.api.base import RestApi

class OmnicOrderSavesnRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.orderId = None
			self.storeId = None
			self.venderStoreId = None
			self.skuId = None
			self.outSkuId = None
			self.sn = None

		def getapiname(self):
			return 'jingdong.omnic.order.savesn'

			





