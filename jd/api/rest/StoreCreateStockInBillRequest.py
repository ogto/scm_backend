from jd.api.base import RestApi

class StoreCreateStockInBillRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.arrivalDay = None
			self.com_id = None
			self.org_id = None
			self.wh_id = None
			self.sku_code = None
			self.num = None
			self.remark = None

		def getapiname(self):
			return 'jingdong.store.createStockInBill'

			





