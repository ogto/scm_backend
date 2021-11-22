from app.main.stores.jd.api.base import RestApi

class LasSpareZerostockStatusSearchRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorCode = None
			self.token = None
			self.serviceNo = None
			self.afsServiceTaskNo = None
			self.orderNo = None
			self.requestTime = None

		def getapiname(self):
			return 'jingdong.las.spare.zerostock.status.search'

			





