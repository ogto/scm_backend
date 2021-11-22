from jd.api.base import RestApi

class DentistryPushGoodsStoreInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.goodsId = None
			self.channelType = None
			self.status = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.dentistry.pushGoodsStoreInfo'

			





