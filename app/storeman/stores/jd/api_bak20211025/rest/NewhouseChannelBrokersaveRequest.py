from app.main.stores.jd.api.base import RestApi

class NewhouseChannelBrokersaveRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.channelId = None
			self.brokerName = None
			self.brokerPhone = None
			self.brokerGender = None
			self.brokerDepartment = None
			self.brokerImg = None
			self.brokerRole = None
			self.imid = None
			self.brokerType = None
			self.businessRecord = None

		def getapiname(self):
			return 'jingdong.newhouse.channel.brokersave'

			





