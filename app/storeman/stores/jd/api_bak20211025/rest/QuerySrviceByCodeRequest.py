from app.main.stores.jd.api.base import RestApi

class QuerySrviceByCodeRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.serviceId = None
			self.venderCode = None
			self.operatorPin = None
			self.operatorName = None

		def getapiname(self):
			return 'jingdong.querySrviceByCode'

			





