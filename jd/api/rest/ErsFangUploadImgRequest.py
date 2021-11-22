from jd.api.base import RestApi

class ErsFangUploadImgRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.urls = None

		def getapiname(self):
			return 'jingdong.ers.fang.uploadImg'

			





