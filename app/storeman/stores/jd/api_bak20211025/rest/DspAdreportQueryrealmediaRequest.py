from app.main.stores.jd.api.base import RestApi

class DspAdreportQueryrealmediaRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.platform = None
			self.pageIndex = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.dsp.adreport.queryrealmedia'

			





