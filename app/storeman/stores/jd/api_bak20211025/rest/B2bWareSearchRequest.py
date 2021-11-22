from app.main.stores.jd.api.base import RestApi

class B2bWareSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelType = None
			self.thirdCid = None
			self.skuSearchTypeEnum = None
			self.pageSize = None
			self.laskSkuId = None
			self.pageNo = None
			self.brandId = None

		def getapiname(self):
			return 'jingdong.b2b.ware.search'

			





