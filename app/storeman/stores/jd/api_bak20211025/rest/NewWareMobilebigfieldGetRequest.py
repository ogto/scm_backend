from app.main.stores.jd.api.base import RestApi

class NewWareMobilebigfieldGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuid = None

		def getapiname(self):
			return 'jingdong.new.ware.mobilebigfield.get'

			





