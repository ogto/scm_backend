from app.main.stores.jd.api.base import RestApi

class AdsDspRtbKeywordPriceUpdateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.ids = None
			self.campaignType = None
			self.putType = None
			self.type = None
			self.change = None
			self.keywordPrice = None
			self.devType = None
			self.groupId = None

		def getapiname(self):
			return 'jingdong.ads.dsp.rtb.keyword.price.update'

			





