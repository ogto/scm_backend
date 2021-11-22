from jd.api.base import RestApi

class ImPopAskRateGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startTime = None
			self.endTime = None

		def getapiname(self):
			return 'jingdong.im.pop.askRate.get'

			





