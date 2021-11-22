from jd.api.base import RestApi

class StoreCountPartitionWhByIdAndStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.status = None

		def getapiname(self):
			return 'jingdong.store.countPartitionWhByIdAndStatus'

			





