from jd.api.base import RestApi

class VcItemPurchasernameGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.purchaser_code = None

		def getapiname(self):
			return 'jingdong.vc.item.purchasername.get'

			





