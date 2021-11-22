from jd.api.base import RestApi

class AdsDspRtbTpBatchUpdateDmpStatusRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.ids = None
			self.operateType = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.batchUpdateDmpStatus'

			





