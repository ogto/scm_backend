from app.main.stores.jd.api.base import RestApi

class OmnichannelStockFullUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.totalItem = None
			self.pageSize = None
			self.pageNo = None
			self.stockType = None
			self.storeId = None
			self.jdSkuId = None
			self.outerSkuId = None
			self.spotStockNum = None
			self.saleStockNum = None
			self.produceStockNum = None
			self.updateTime = None

		def getapiname(self):
			return 'jingdong.omnichannel.stock.full.update'

			





