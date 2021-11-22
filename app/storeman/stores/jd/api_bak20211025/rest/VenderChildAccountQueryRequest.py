from app.main.stores.jd.api.base import RestApi

class VenderChildAccountQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.size = None

		def getapiname(self):
			return 'jingdong.vender.childAccount.query'

			





