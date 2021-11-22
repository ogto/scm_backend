from jd.api.base import RestApi

class CmpArticleSaveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.summary = None
			self.saveType = None
			self.publishTime = None
			self.dpContent = None
			self.skuStr = None
			self.businessId = None
			self.threeDskuStr = None
			self.threeDimensionalImgInfo = None
			self.title = None
			self.titlePicUrl = None
			self.content = None
			self.support3d = None
			self.labelIds = None
			self.articleType = None
			self.id = None
			self.channelId = None

		def getapiname(self):
			return 'jingdong.cmp.article.save'

			





