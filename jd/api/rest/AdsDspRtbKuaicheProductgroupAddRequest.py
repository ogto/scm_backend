from jd.api.base import RestApi

class AdsDspRtbKuaicheProductgroupAddRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.fee = None
			self.inSearchFee = None
			self.campaignId = None
			self.mobilePriceCoef = None
			self.name = None
			self.newAreaIds = None
			self.skuId = None
			self.adName = None
			self.imgUrl = None
			self.customTitle = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.kuaiche.productgroup.add'

			





