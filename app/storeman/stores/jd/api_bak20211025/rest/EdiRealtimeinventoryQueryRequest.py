from app.main.stores.jd.api.base import RestApi

class EdiRealtimeinventoryQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operatorErp = None
			self.jdSku = None
			self.vendorCode = None

		def getapiname(self):
			return 'jingdong.edi.realtimeinventory.query'

			





