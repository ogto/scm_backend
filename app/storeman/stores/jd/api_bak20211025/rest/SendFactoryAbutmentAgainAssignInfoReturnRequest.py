from app.main.stores.jd.api.base import RestApi

class SendFactoryAbutmentAgainAssignInfoReturnRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.auth_no = None
			self.msg_type = None
			self.ord_no = None
			self.assign_time = None
			self.at_home_time = None
			self.assigner_name = None
			self.assigner_tel = None

		def getapiname(self):
			return 'jingdong.sendFactoryAbutmentAgainAssignInfoReturn'

			





