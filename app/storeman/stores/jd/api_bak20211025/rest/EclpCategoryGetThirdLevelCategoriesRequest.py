from app.main.stores.jd.api.base import RestApi

class EclpCategoryGetThirdLevelCategoriesRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.secondCategoryNo = None
			self.thirdCategoryNo = None

		def getapiname(self):
			return 'jingdong.eclp.category.getThirdLevelCategories'

			





