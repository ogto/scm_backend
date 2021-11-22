from app.main.stores.jd.api.base import RestApi

class B2bPromotionPriceGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.param = None

		def getapiname(self):
			return 'jingdong.b2b.promotion.price.get'

			
	

class PlatformInfo(object):
		def __init__(self):
			"""
			"""
			self.platform = None
			self.channel = None


class UserInfo(object):
		def __init__(self):
			"""
			"""
			self.pin = None
			self.ip = None


class AreaInfo(object):
		def __init__(self):
			"""
			"""
			self.provinceId = None
			self.cityId = None
			self.countyId = None
			self.townId = None


class Param(object):
		def __init__(self):
			"""
			"""
			self.sku = None
			self.platformInfo = None
			self.userInfo = None
			self.num = None
			self.areaInfo = None
			self.extParam = None





