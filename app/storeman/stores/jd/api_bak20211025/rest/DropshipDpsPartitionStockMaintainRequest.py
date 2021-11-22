from app.main.stores.jd.api.base import RestApi

class DropshipDpsPartitionStockMaintainRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sku = None
			self.stockNum = None
			self.storeId = None
			self.rfId = None

		def getapiname(self):
			return 'jingdong.dropship.dps.partitionStock.maintain'

			





