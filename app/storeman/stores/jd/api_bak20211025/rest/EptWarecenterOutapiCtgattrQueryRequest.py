from app.main.stores.jd.api.base import RestApi

class EptWarecenterOutapiCtgattrQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.catId = None

		def getapiname(self):
			return 'jingdong.ept.warecenter.outapi.ctgattr.query'

			





