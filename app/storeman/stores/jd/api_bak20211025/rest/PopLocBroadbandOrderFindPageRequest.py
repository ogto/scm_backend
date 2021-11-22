from app.main.stores.jd.api.base import RestApi

class PopLocBroadbandOrderFindPageRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_created_begin = None
			self.order_created_end = None
			self.order_status = None
			self.page = None
			self.page_size = None

		def getapiname(self):
			return 'jingdong.pop.loc.broadband.order.findPage'

			





