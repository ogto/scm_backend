from jd.api.base import RestApi

class PresortSitefenceimportServiceRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operationType = None
			self.siteCode = None
			self.siteName = None
			self.siteLocation = None
			self.fenceNum = None
			self.fenceArray = None

		def getapiname(self):
			return 'jingdong.presort.sitefenceimport.service'

			





