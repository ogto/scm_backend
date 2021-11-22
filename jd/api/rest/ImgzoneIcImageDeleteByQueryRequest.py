from jd.api.base import RestApi

class ImgzoneIcImageDeleteByQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.imgId = None
			self.imgJfsKey = None
			self.operate = None

		def getapiname(self):
			return 'jingdong.imgzone.ic.image.deleteByQuery'

			





