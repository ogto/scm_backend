from app.main.stores.jd.api.base import RestApi

class HouseDataPublishSaasValidBrokerIfRegisterRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.phone = None

		def getapiname(self):
			return 'jingdong.house.data.publish.saas.validBrokerIfRegister'

			





