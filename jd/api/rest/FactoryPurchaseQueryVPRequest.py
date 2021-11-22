from jd.api.base import RestApi

class FactoryPurchaseQueryVPRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.factoryId = None
			self.personalKey = None
			self.ptId = None
			self.vendorCode = None
			self.vendorName = None
			self.vendorNameAbbr = None
			self.code = None
			self.name = None
			self.categoryId = None
			self.parentCategoryId = None
			self.rootCategoryId = None
			self.skuId = None
			self.skuName = None
			self.purchaseMan = None
			self.skuType = None
			self.available = None
			self.createdStart = None
			self.createdEnd = None
			self.stockInVendor = None
			self.modifiedStart = None
			self.modifiedEnd = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.factory.purchase.queryVP'

			





