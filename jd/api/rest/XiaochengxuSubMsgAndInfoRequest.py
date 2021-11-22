from jd.api.base import RestApi

class XiaochengxuSubMsgAndInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.userPin = None
			self.modelId = None
			self.pushType = None
			self.onOff = None

		def getapiname(self):
			return 'jingdong.xiaochengxu.subMsgAndInfo'

			





