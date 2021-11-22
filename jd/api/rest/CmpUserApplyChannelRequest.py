from jd.api.base import RestApi

class CmpUserApplyChannelRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.summary = None
			self.id = None
			self.nickName = None
			self.headPicUrl = None
			self.userSource = None
			self.type = None
			self.designerType = None

		def getapiname(self):
			return 'jingdong.cmp.user.apply.channel'

			





