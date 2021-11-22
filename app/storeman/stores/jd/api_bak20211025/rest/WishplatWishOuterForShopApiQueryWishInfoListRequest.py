from app.main.stores.jd.api.base import RestApi

class WishplatWishOuterForShopApiQueryWishInfoListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.pageSize = None
			self.wishTypeId = None
			self.startDate = None
			self.endDate = None

		def getapiname(self):
			return 'jingdong.wishplat.wishOuterForShopApi.queryWishInfoList'

			





