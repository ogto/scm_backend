from app.main.stores.jd.api.base import RestApi

class DspAdkckeywordKeywordpricesuggestQueryRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.key = None
			self.mobileType = None

		def getapiname(self):
			return 'jingdong.dsp.adkckeyword.keywordpricesuggest.query'

			





