from app.main.stores.jd.api.base import RestApi

class WareReadFindWareByIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.field = None

		def getapiname(self):
			return 'jingdong.ware.read.findWareById'

			





