from jd.api.base import RestApi

class ImageWriteDeleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.colorIds = None
			self.imgIndexes = None

		def getapiname(self):
			return 'jingdong.image.write.delete'

			





