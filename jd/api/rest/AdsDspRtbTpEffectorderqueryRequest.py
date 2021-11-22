from jd.api.base import RestApi

class AdsDspRtbTpEffectorderqueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignId = None
			self.clickOrOrderDay = None
			self.deliveryType = None
			self.endClickDay = None
			self.endOrderDay = None
			self.giftFlag = None
			self.groupId = None
			self.orderStatus = None
			self.orderType = None
			self.page = None
			self.pageSize = None
			self.province = None
			self.startClickDay = None
			self.startOrderDay = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.effectorderquery'

			





