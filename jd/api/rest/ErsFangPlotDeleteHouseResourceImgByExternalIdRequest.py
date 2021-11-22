from jd.api.base import RestApi

class ErsFangPlotDeleteHouseResourceImgByExternalIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.cityCode = None
			self.sourceId = None
			self.pSourceId = None

		def getapiname(self):
			return 'jingdong.ers.fang.plot.deleteHouseResourceImgByExternalId'

			





