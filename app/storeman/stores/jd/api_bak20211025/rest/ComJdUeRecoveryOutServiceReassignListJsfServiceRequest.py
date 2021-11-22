from app.main.stores.jd.api.base import RestApi

class ComJdUeRecoveryOutServiceReassignListJsfServiceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.code = None
			self.data = None

		def getapiname(self):
			return 'jingdong.com.jd.ue.recovery.out.service.ReassignListJsfService'

			





