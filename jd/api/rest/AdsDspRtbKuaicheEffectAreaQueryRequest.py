from jd.api.base import RestApi

class AdsDspRtbKuaicheEffectAreaQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.clickOrOrderDay = None
			self.giftFlag = None
			self.orderStatusCategory = None
			self.endDay = None
			self.isDaily = None
			self.startDay = None
			self.platform = None
			self.clickOrOrderCaliber = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.effectAreaQuery'

			





