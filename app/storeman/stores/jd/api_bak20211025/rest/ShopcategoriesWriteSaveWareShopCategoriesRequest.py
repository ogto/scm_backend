from app.main.stores.jd.api.base import RestApi

class ShopcategoriesWriteSaveWareShopCategoriesRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.shopCategory = None

		def getapiname(self):
			return 'jingdong.shopcategories.write.saveWareShopCategories'

			





