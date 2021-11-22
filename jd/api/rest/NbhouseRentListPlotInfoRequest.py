from jd.api.base import RestApi

class NbhouseRentListPlotInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.lat = None
			self.lon = None
			self.distance = None
			self.plotName = None
			self.plotCode = None
			self.matchName = None
			self.currentPage = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.nbhouse.rent.listPlotInfo'

			





