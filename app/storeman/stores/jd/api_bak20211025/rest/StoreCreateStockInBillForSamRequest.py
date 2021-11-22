from app.main.stores.jd.api.base import RestApi

class StoreCreateStockInBillForSamRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sam_bill_id = None
			self.arrivalDay = None
			self.club_id = None
			self.item_id = None
			self.num = None
			self.remark = None
			self.samStoreType = None

		def getapiname(self):
			return 'jingdong.store.createStockInBillForSam'

			





