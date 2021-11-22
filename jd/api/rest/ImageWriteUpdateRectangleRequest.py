from jd.api.base import RestApi

class ImageWriteUpdateRectangleRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.colorId = None
			self.imgId = None
			self.imgRectangleUrl = None
			self.imgIndex = None

		def getapiname(self):
			return 'jingdong.image.write.updateRectangle'

			





