from jd.api.base import RestApi

class TransparentImageWriteSaveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.colorId = None
			self.imageUrl = None

		def getapiname(self):
			return 'jingdong.transparentImage.write.save'

			





