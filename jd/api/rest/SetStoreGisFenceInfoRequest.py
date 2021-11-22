from jd.api.base import RestApi

class SetStoreGisFenceInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.kilometres = None
			self.vertexs = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.setStoreGisFenceInfo'

			





