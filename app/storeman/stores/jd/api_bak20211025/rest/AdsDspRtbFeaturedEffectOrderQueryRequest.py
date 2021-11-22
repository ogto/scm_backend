from app.main.stores.jd.api.base import RestApi

class AdsDspRtbFeaturedEffectOrderQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.pageSize = None
			self.clickOrOrderDay = None
			self.impressionOrClickEffect = None
			self.campaignId = None
			self.groupId = None
			self.orderStartDay = None
			self.orderEndDay = None
			self.cilckStartDay = None
			self.cilckEndDay = None
			self.mySelf = None
			self.clickOrOrderCaliber = None
			self.province = None
			self.posPackageId = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.featured.effectOrderQuery'

			





