from jd.api.base import RestApi

class VenderShopcategoryDeleteShopCategoryByVenderIdAndCidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cid = None

		def getapiname(self):
			return 'jingdong.vender.shopcategory.deleteShopCategoryByVenderIdAndCid'

			





