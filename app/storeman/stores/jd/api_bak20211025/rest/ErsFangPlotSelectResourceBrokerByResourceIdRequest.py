from app.main.stores.jd.api.base import RestApi

class ErsFangPlotSelectResourceBrokerByResourceIdRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.pSourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.plot.selectResourceBrokerByResourceId'

			





