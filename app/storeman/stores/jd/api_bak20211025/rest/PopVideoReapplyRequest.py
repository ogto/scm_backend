from app.main.stores.jd.api.base import RestApi

class PopVideoReapplyRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.video_id = None
			self.apply_reason = None

		def getapiname(self):
			return 'jingdong.pop.video.reapply'

			





