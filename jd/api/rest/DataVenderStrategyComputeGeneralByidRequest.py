from jd.api.base import RestApi

class DataVenderStrategyComputeGeneralByidRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.strategy_id = None
			self.strategy_param = None
			self.pin_type = None

		def getapiname(self):
			return 'jingdong.data.vender.strategy.compute.general.byid'

			





