from jd.api.base import RestApi

class JlMemberUserextQueryByMobileRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.mobile = None
			self.platformId = None

		def getapiname(self):
			return 'jingdong.jl.member.userext.queryByMobile'

			





