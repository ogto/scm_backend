from app.main.stores.jd.api.base import RestApi

class ErsFangAddCityAreaRateRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.averageRate = None
			self.linkRelativeRate = None
			self.rateDate = None

		def getapiname(self):
			return 'jingdong.ers.fang.addCityAreaRate'

			





