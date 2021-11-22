from app.main.stores.jd.api.base import RestApi

class AdsDspRtbTpBatchDeleteDmpRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.adGroupId = None
			self.ids = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.batchDeleteDmp'

			





