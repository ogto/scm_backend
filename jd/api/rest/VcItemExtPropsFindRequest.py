from jd.api.base import RestApi

class VcItemExtPropsFindRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.category_leaf_id = None

		def getapiname(self):
			return 'jingdong.vc.item.extProps.find'

			





