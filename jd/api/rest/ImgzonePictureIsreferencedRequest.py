from jd.api.base import RestApi

class ImgzonePictureIsreferencedRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.picture_id = None

		def getapiname(self):
			return 'jingdong.imgzone.picture.isreferenced'

			





