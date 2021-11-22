from app.main.stores.jd.api.base import RestApi

class AdwordsWriteUpdateWareAdWordsRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.url = None
			self.urlWords = None
			self.words = None

		def getapiname(self):
			return 'jingdong.adwords.write.updateWareAdWords'

			





