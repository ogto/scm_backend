from app.main.stores.jd.api.base import RestApi

class AllotEngineerRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.serviceId = None
			self.operatorName = None
			self.operatorPin = None
			self.engineerPin = None
			self.engineerName = None
			self.venderCode = None

		def getapiname(self):
			return 'jingdong.allotEngineer'

			





