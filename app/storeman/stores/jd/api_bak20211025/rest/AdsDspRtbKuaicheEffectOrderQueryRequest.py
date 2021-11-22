from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKuaicheEffectOrderQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pageSize = None
			self.clickOrOrderDay = None
			self.giftFlag = None
			self.endClickDay = None
			self.isDaily = None
			self.startClickDay = None
			self.page = None
			self.platform = None
			self.campaignId = None
			self.deliveryType = None
			self.groupId = None
			self.orderType = None
			self.orderStatus = None
			self.province = None
			self.startOrderDay = None
			self.endOrderDay = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.effectOrderQuery'

			





