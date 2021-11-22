from app.main.stores.jd.api.base import RestApi

class VcConfirmpurchaseorderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_id = None
			self.delivery_time = None
			self.ware_id = None
			self.confirm_num = None
			self.back_explanation = None
			self.back_explanation_type = None
			self.deliver_center_id = None

		def getapiname(self):
			return 'jingdong.vc.confirmpurchaseorder'

			





