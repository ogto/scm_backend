from app.storeman.stores.jd.api.base import RestApi

class CategoryReadFindAttrsByCategoryIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cid = None
			self.attributeType = None
			self.field = None

		def getapiname(self):
			return 'jingdong.category.read.findAttrsByCategoryId'

			





