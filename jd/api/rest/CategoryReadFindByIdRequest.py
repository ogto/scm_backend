from jd.api.base import RestApi

class CategoryReadFindByIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cid = None
			self.field = None

		def getapiname(self):
			return 'jingdong.category.read.findById'

			





