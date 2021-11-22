from jd.api.base import RestApi

class HealthcarePushGoodsStoreInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.goodsId = None
			self.status = None
			self.channelType = None
			self.storeId = None
			self.vipType = None

		def getapiname(self):
			return 'jingdong.healthcare.pushGoodsStoreInfo'

			





