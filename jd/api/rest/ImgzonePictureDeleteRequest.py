from jd.api.base import RestApi

class ImgzonePictureDeleteRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.picture_ids = None

		def getapiname(self):
			return 'jingdong.imgzone.picture.delete'

			





