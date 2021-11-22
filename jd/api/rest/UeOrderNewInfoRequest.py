from jd.api.base import RestApi

class UeOrderNewInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.siteInfoList = None

		def getapiname(self):
			return 'jingdong.ue.order.new.info'

			
	

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
			self.pid = None
			self.engineerName = None
			self.engineerMobile = None


class SiteInfo(object):
		def __init__(self):
			"""
			"""
			self.siteCode = None
			self.address = None
			self.siteTown = None
			self.siteCity = None
			self.serviceAreaList = None
			self.siteCounty = None
			self.siteName = None
			self.serviceCatList = None
			self.contactMan = None
			self.siteProvince = None
			self.siteMobile = None
			self.venderCode = None
			self.appid = None
			self.engineerInfoList = None
			self.unifiedCode = None
			self.personName = None
			self.personMobile = None
			self.personPib = None
			self.accountName = None
			self.bankCode = None
			self.bankName = None
			self.dutyParagraph = None
			self.bankAccount = None





