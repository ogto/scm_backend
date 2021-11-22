from jd.api.base import RestApi

class StoreQueryStockInBillRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.stock_in_status = None
			self.stock_in_bill_id = None
			self.com_id = None
			self.org_id = None
			self.wh_id = None
			self.sku_id = None
			self.begin_time = None
			self.end_time = None
			self.page = None
			self.page_size = None

		def getapiname(self):
			return 'jingdong.store.queryStockInBill'

			





