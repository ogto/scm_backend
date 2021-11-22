from app.storeman.stores.jd.api.base import RestApi

class ImageWriteUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.colorId = None
			self.imgId = None
			self.imgIndex = None
			self.imgUrl = None
			self.imgZoneId = None

		def getapiname(self):
			return 'jingdong.image.write.update'

			





