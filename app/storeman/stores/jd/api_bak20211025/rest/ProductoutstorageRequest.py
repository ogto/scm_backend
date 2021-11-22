from app.main.stores.jd.api.base import RestApi

class ProductoutstorageRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.twoOrderId = None
			self.waybillNumber = None
			self.logisticsCompanies = None
			self.bagCount = None
			self.extStr = None

		def getapiname(self):
			return 'jingdong.productoutstorage'

			





