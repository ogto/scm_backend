from jd.api.base import RestApi

class GwsJzoneSendWxTemplateMessageByPinRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channel = None
			self.pin = None
			self.appId = None
			self.color = None
			self.name = None
			self.value = None
			self.msgUrl = None
			self.templateId = None
			self.shortTemplateId = None
			self.open_id_buyer = None
			self.xid_buyer = None

		def getapiname(self):
			return 'jingdong.gws.jzone.sendWxTemplateMessageByPin'

			





