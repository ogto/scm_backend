from app.main.stores.jd.api.base import RestApi

class AdsDspRtbTpDeliveryListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.campaignType = None
			self.billingType = None
			self.clickOrOrderDay = None
			self.clickOrOrderCaliber = None
			self.giftFlag = None
			self.orderStatusCategory = None
			self.startDay = None
			self.endDay = None
			self.nameLike = None
			self.page = None
			self.pageSize = None
			self.campaignId = None
			self.groupId = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.tp.deliveryList'

			





