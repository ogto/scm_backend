from jd.api.base import RestApi

class B2bPoPoMidProviderQueryPurOrderDetailRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.poId = None
			self.tagName = None

		def getapiname(self):
			return 'jingdong.b2b.po.PoMidProvider.queryPurOrderDetail'

			





