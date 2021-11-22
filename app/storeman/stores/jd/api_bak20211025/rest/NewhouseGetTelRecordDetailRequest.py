from app.main.stores.jd.api.base import RestApi

class NewhouseGetTelRecordDetailRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelId = None
			self.clueId = None

		def getapiname(self):
			return 'jingdong.newhouse.getTelRecordDetail'

			





