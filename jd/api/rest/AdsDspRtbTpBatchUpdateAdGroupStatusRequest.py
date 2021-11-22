from jd.api.base import RestApi

class AdsDspRtbTpBatchUpdateAdGroupStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.idList = None
			self.status = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.batchUpdateAdGroupStatus'

			





