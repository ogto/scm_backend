from app.main.stores.jd.api.base import RestApi

class GetUserPlusLevelQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.fields = None

		def getapiname(self):
			return 'jingdong.getUserPlusLevel.query'

			





