from jd.api.base import RestApi

class UserGetUserInfoByXIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.XId = None

		def getapiname(self):
			return 'jingdong.user.getUserInfoByXId'

			





