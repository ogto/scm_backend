from app.main.stores.jd.api.base import RestApi

class VcGetpurchaseorderlistRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.created_date_start = None
			self.created_date_end = None
			self.deliver_center_id = None
			self.status = None
			self.is_ept_customized = None
			self.page_index = None
			self.page_size = None
			self.orderIds = None
			self.wareIds = None
			self.states = None
			self.confirmStates = None

		def getapiname(self):
			return 'jingdong.vc.getpurchaseorderlist'

			





