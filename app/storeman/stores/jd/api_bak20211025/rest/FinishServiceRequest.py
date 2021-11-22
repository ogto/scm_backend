from app.main.stores.jd.api.base import RestApi

class FinishServiceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderCode = None
			self.serviceId = None
			self.engineerPin = None
			self.engineerName = None
			self.finshNum = None
			self.remart = None

		def getapiname(self):
			return 'jingdong.finishService'

			





