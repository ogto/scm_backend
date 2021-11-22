from app.main.stores.jd.api.base import RestApi

class UeOrderInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.siteInfoList = None

		def getapiname(self):
			return 'jingdong.ue.order.info'

			
	

class ServiceArea(object):
		def __init__(self):
			"""
			"""
			self.province = None
			self.town = None
			self.city = None
			self.county = None


class ServiceCat(object):
		def __init__(self):
			"""
			"""
			self.serviceQty = None
			self.secondLevelCat = None
			self.firstLevelCat = None
			self.thirdLevelCat = None


class EngineerInfo(object):
		def __init__(self):
			"""
			"""
			self.engineerCode = None
			self.engineerName = None
			self.engineerMobile = None


class SiteInfo(object):
		def __init__(self):
			"""
			"""
			self.siteCode = None
			self.address = None
			self.town = None
			self.city = None
			self.serviceAreaList = None
			self.county = None
			self.siteName = None
			self.serviceCatList = None
			self.contactMan = None
			self.province = None
			self.siteMobile = None
			self.appid = None
			self.engineerInfoList = None





