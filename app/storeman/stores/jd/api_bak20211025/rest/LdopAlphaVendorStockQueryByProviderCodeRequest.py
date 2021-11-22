from app.main.stores.jd.api.base import RestApi

class LdopAlphaVendorStockQueryByProviderCodeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorCode = None
			self.providerCode = None
			self.branchCode = None

		def getapiname(self):
			return 'jingdong.ldop.alpha.vendor.stock.queryByProviderCode'

			





