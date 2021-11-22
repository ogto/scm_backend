from app.storeman.stores.jd.api.base import RestApi

class ImageReadFindImagesByWareIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None

		def getapiname(self):
			return 'jingdong.image.read.findImagesByWareId'

			





