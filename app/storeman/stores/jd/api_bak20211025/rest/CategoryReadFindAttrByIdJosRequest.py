from app.main.stores.jd.api.base import RestApi

class CategoryReadFindAttrByIdJosRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.attrId = None
			self.field = None

		def getapiname(self):
			return 'jingdong.category.read.findAttrByIdJos'

			




