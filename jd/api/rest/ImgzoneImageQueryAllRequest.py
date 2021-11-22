from jd.api.base import RestApi

class ImgzoneImageQueryAllRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.category_id = None
			self.image_name = None
			self.scroll_id = None

		def getapiname(self):
			return 'jingdong.imgzone.image.queryAll'

			





