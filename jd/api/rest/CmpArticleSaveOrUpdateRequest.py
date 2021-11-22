from jd.api.base import RestApi

class CmpArticleSaveOrUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.summary = None
			self.provinceId = None
			self.houseArea = None
			self.labelIds = None
			self.cityId = None
			self.houseBudget = None
			self.submitTime = None
			self.cityName = None
			self.skuList = None
			self.provinceName = None
			self.saveType = None
			self.id = None
			self.content = None
			self.districtName = None
			self.title = None
			self.districtId = None
			self.source = None
			self.titlePicUrl = None
			self.articleType = None

		def getapiname(self):
			return 'jingdong.cmp.article.saveOrUpdate'

			





