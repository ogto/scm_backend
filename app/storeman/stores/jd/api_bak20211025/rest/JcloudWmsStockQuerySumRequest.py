from app.main.stores.jd.api.base import RestApi

class JcloudWmsStockQuerySumRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuNo = None
			self.ownerNo = None
			self.warehouseNo = None
			self.tenantId = None

		def getapiname(self):
			return 'jingdong.jcloud.wms.stock.query.sum'

			





