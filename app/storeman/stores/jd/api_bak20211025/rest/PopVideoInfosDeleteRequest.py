from app.main.stores.jd.api.base import RestApi

class PopVideoInfosDeleteRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.video_ids = None

		def getapiname(self):
			return 'jingdong.pop.video.infos.delete'

			





