from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKcAdUpdateStatusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operateType = None
			self.adIds = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kc.ad.updateStatus'

			





