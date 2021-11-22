from jd.api.base import RestApi

class ErsFangAddOrUpdateChannelRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.sourceId = None
			self.businessType = None
			self.channelName = None
			self.businessLicense = None
			self.cityName = None
			self.companyLogo = None
			self.companyDes = None
			self.purAgentRate = None
			self.sellAgentRate = None
			self.purCagentDes = None
			self.sellCagentDes = None

		def getapiname(self):
			return 'jingdong.ers.fang.addOrUpdateChannel'

			





