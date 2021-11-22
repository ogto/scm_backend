from jd.api.base import RestApi

class NewhouseSynHouseClueStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.clueId = None
			self.clueStatus = None
			self.brokerId = None
			self.updateTimeLong = None
			self.channelId = None
			self.visitQrCode = None
			self.protectionDeadlineLong = None
			self.propertyConsultantName = None
			self.propertyConsultantPhone = None

		def getapiname(self):
			return 'jingdong.newhouse.synHouseClueStatus'

			





