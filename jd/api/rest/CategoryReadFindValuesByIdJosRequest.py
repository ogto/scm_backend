from jd.api.base import RestApi

class CategoryReadFindValuesByIdJosRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.field = None

		def getapiname(self):
			return 'jingdong.category.read.findValuesByIdJos'

			




