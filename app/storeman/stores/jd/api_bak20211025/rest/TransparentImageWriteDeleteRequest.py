from app.main.stores.jd.api.base import RestApi

class TransparentImageWriteDeleteRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.colorId = None

		def getapiname(self):
			return 'jingdong.transparentImage.write.delete'

			





