from app.main.stores.jd.api.base import RestApi

class RetailerCompanyCustomSelectInfosRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sellerId = None

		def getapiname(self):
			return 'jingdong.retailer.company.custom.select.infos'

			




