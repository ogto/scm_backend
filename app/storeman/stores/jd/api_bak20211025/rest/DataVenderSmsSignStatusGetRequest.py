from app.main.stores.jd.api.base import RestApi

class DataVenderSmsSignStatusGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channel = None

		def getapiname(self):
			return 'jingdong.data.vender.sms.sign.status.get'

			





