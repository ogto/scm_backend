from app.main.stores.jd.api.base import RestApi

class AssetBenefitOrderQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.request_id = None

		def getapiname(self):
			return 'jingdong.asset.benefit.order.query'

			





