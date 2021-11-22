from app.main.stores.jd.api.base import RestApi

class NewhouseBindOuterBroker2SpuRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.paramInfo = None

		def getapiname(self):
			return 'jingdong.newhouse.bindOuterBroker2Spu'

			





