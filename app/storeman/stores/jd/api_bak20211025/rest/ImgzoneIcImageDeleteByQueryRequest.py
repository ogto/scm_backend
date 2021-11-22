from app.main.stores.jd.api.base import RestApi

class ImgzoneIcImageDeleteByQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.imgId = None
			self.imgJfsKey = None
			self.operate = None

		def getapiname(self):
			return 'jingdong.imgzone.ic.image.deleteByQuery'

			





