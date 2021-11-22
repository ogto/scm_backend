from jd.api.base import RestApi

class AdsDspRtbTpBatchUpdateAdStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adIds = None
			self.status = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.batchUpdateAdStatus'

			





