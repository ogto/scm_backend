from jd.api.base import RestApi

class VenderReturnaddressQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.address_type = None

		def getapiname(self):
			return 'jingdong.vender.returnaddress.query'

			





