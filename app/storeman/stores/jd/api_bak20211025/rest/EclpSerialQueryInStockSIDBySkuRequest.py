from app.main.stores.jd.api.base import RestApi

class EclpSerialQueryInStockSIDBySkuRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.goodsNo = None
			self.pageNo = None
			self.pageSize = None
			self.queryType = None

		def getapiname(self):
			return 'jingdong.eclp.serial.queryInStockSIDBySku'

			





