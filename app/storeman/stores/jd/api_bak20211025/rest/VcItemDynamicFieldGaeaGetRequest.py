from app.main.stores.jd.api.base import RestApi

class VcItemDynamicFieldGaeaGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cid3 = None

		def getapiname(self):
			return 'jingdong.vc.item.dynamicFieldGaea.get'

			





