from app.main.stores.jd.api.base import RestApi

class DentistryPushGoodsInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ThirdGoodsParam = None

		def getapiname(self):
			return 'jingdong.dentistry.pushGoodsInfo'

			
	

class ThirdGoodsItemParam(object):
		def __init__(self):
			"""
			"""
			self.itemName = None
			self.itemDesc = None


class ThirdGoodsParam(object):
		def __init__(self):
			"""
			"""
			self.goodsId = None
			self.channelType = None
			self.operateType = None
			self.status = None
			self.goodsSuitable = None
			self.goodsPrice = None
			self.goodsFeature = None
			self.goodsName = None
			self.goodsItemList = None





