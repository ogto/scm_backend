from jd.api.base import RestApi

class PopVideoInfoQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.video_name = None
			self.status = None
			self.statuses = None
			self.agent_video_id = None
			self.video_type = None
			self.created_date_start = None
			self.created_date_end = None
			self.order = None
			self.order_by = None
			self.page_index = None
			self.page_size = None
			self.sku_id = None

		def getapiname(self):
			return 'jingdong.pop.video.info.query'

			





