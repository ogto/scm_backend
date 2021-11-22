from app.main.stores.jd.api.base import RestApi

class VcCreatepurchaseorderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_deliver_center_id = None
			self.purchaser_erp_code = None
			self.order_remark = None
			self.ware_id = None
			self.ware_deliver_center_id = None
			self.original_num = None
			self.ware_remark = None

		def getapiname(self):
			return 'jingdong.vc.createpurchaseorder'

			





