from jd.api.base import RestApi

class ErsFangDeletePlotBrokerByExternalIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.sourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.deletePlotBrokerByExternalId'

			





