from jd.api.base import RestApi

class NewhouseBindingSpuBrokerRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.v1 = None
			self.channelId = None
			self.spuId = None

		def getapiname(self):
			return 'jingdong.newhouse.bindingSpuBroker'

			





