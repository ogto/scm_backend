from app.main.stores.jd.api.base import RestApi

class ErsFangAddOrUpdatePlotBrokerRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.brokerId = None
			self.plotId = None
			self.recommend = None
			self.cityCode = None
			self.sourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.addOrUpdatePlotBroker'

			





