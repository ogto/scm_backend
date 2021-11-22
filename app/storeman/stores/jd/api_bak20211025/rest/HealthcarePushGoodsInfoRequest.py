from app.main.stores.jd.api.base import RestApi

class HealthcarePushGoodsInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ThirdGoodsParam = None

		def getapiname(self):
			return 'jingdong.healthcare.pushGoodsInfo'

			
	

class ThirdGoodsItemParam(object):
		def __init__(self):
			"""
			"""
			self.itemMeans = None
			self.itemName = None
			self.itemTopCategory = None
			self.goodsId2 = None
			self.itemSuitable2 = None
			self.itemSecCategory = None


class ThirdGoodsParam(object):
		def __init__(self):
			"""
			"""
			self.goodsItemList = None
			self.goodsId = None
			self.goodsPrice = None
			self.operateType = None
			self.goodsFeature = None
			self.goodsName = None
			self.status = None
			self.channelType = None
			self.goodsSuitable = None
			self.goodsMarry = None





