from jd.api.base import RestApi

class ErsFangAddHousesResourceRateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.channelId = None
			self.totalPrice = None
			self.cityCode = None
			self.pSourceId = None
			self.sourceId = None
			self.rateDate = None

		def getapiname(self):
			return 'jingdong.ers.fang.addHousesResourceRate'

			





