from app.main.stores.jd.api.base import RestApi

class EdiRoDetailBatchGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.returnOrderCode = None
			self.jdSku = None

		def getapiname(self):
			return 'jingdong.edi.ro.detail.batch.get'

			





