from jd.api.base import RestApi

class PrepushinformationdatatestRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.dataType = None
			self.jsonData = None
			self.extStr = None

		def getapiname(self):
			return 'jingdong.prepushinformationdatatest'

			





