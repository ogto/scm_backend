from jd.api.base import RestApi

class SellerVenderInfoGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ext_json_param = None

		def getapiname(self):
			return 'jingdong.seller.vender.info.get'

			





