from app.main.stores.jd.api.base import RestApi

class UpdateStoreStatusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.param = None

		def getapiname(self):
			return 'jingdong.updateStoreStatus'

			
	

class Param(object):
		def __init__(self):
			"""
			"""
			self.storeStatus = None
			self.id = None





