from app.main.stores.jd.api.base import RestApi

class EdiScDetailGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.purchaseOrderCode = None

		def getapiname(self):
			return 'jingdong.edi.sc.detail.get'

			





