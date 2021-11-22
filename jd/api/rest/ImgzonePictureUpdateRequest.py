from jd.api.base import RestApi

class ImgzonePictureUpdateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.picture_id = None
			self.picture_name = None
			self.picture_cate_id = None

		def getapiname(self):
			return 'jingdong.imgzone.picture.update'

			





