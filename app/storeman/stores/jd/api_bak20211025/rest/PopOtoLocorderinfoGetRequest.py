from app.main.stores.jd.api.base import RestApi

class PopOtoLocorderinfoGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_id = None
			self.code_type = None

		def getapiname(self):
			return 'jingdong.pop.oto.locorderinfo.get'

			





