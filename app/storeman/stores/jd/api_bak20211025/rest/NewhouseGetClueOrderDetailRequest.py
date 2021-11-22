from app.main.stores.jd.api.base import RestApi

class NewhouseGetClueOrderDetailRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.clueId = None
			self.channelId = None

		def getapiname(self):
			return 'jingdong.newhouse.getClueOrderDetail'

			





