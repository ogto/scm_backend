from jd.api.base import RestApi

class VcGetdetailbyorderidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_id = None
			self.sort_filed = None
			self.sort_mode = None
			self.page_index = None
			self.page_size = None
			self.is_page = None

		def getapiname(self):
			return 'jingdong.vc.getdetailbyorderid'

			





