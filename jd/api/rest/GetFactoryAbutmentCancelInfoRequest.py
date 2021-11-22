from jd.api.base import RestApi

class GetFactoryAbutmentCancelInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authorizedSequence = None

		def getapiname(self):
			return 'jingdong.getFactoryAbutmentCancelInfo'

			





