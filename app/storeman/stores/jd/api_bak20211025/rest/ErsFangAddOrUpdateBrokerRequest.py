from app.main.stores.jd.api.base import RestApi

class ErsFangAddOrUpdateBrokerRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelId = None
			self.name = None
			self.extensionNum = None
			self.extensionPhone = None
			self.phoneNum = None
			self.headImg = None
			self.infoCard = None
			self.businessLicense = None
			self.cityName = None
			self.areaName = None
			self.company = None
			self.tradingAreaId = None
			self.shop = None
			self.declaration = None
			self.speciality = None
			self.seniority = None
			self.workHours = None
			self.workingExperience = None
			self.brokerStatus = None
			self.cityCode = None
			self.sourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.addOrUpdateBroker'

			





