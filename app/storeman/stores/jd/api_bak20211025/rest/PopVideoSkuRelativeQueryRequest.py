from app.main.stores.jd.api.base import RestApi

class PopVideoSkuRelativeQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.video_id = None
			self.product_id = None
			self.sku_id = None
			self.status = None
			self.statuses = None
			self.videoType = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.pop.video.sku.relative.query'

			





