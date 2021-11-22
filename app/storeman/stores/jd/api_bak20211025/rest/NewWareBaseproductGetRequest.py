from app.main.stores.jd.api.base import RestApi

class NewWareBaseproductGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ids = None
			self.basefields = None

		def getapiname(self):
			return 'jingdong.new.ware.baseproduct.get'

			





