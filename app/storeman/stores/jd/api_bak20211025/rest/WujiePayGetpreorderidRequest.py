from app.main.stores.jd.api.base import RestApi

class WujiePayGetpreorderidRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.brandId = None
			self.bizId = None
			self.exStoreId = None
			self.outTradeNo = None
			self.amount = None
			self.notifyUrl = None
			self.extMap = None
			self.merchantNo = None
			self.storePrice = None
			self.exSkuId = None
			self.count = None
			self.activityPrice = None
			self.returnUrl = None
			self.venderId = None
			self.scene = None
			self.activityAmount = None

		def getapiname(self):
			return 'jingdong.wujie.pay.getpreorderid'

			





