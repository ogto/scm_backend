from jd.api.base import RestApi

class EdiRoDetailGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.returnOrderCode = None

		def getapiname(self):
			return 'jingdong.edi.ro.detail.get'

			





