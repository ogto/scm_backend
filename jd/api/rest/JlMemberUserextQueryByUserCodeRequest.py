from jd.api.base import RestApi

class JlMemberUserextQueryByUserCodeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.platformId = None
			self.userCode = None

		def getapiname(self):
			return 'jingdong.jl.member.userext.queryByUserCode'

			





