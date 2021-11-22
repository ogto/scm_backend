from jd.api.base import RestApi

class RetailerCompanyCustomSelectInfosRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sellerId = None

		def getapiname(self):
			return 'jingdong.retailer.company.custom.select.infos'

			





