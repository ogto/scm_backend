from app.main.stores.jd.api.base import RestApi

class PopCrmGetMemberInVenderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customerPin = None
			self.open_id_buyer = None

		def getapiname(self):
			return 'jingdong.pop.crm.getMemberInVender'

			





