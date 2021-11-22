from app.main.stores.jd.api.base import RestApi

class AdsDspRtbHtGetSkuEffectReportRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.activityId = None
			self.campaignId = None
			self.clickOrOrderDay = None
			self.clickStartDay = None
			self.clickEndDay = None
			self.orderStartDay = None
			self.orderEndDay = None
			self.orderStatus = None
			self.page = None
			self.pageSize = None
			self.platform = None
			self.province = None
			self.giftFlag = None
			self.mySelf = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.ht.getSkuEffectReport'

			





