from jd.api.base import RestApi

class PopVenderCenerVenderBrandQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.name = None

		def getapiname(self):
			return 'jingdong.pop.vender.cener.venderBrand.query'

			





