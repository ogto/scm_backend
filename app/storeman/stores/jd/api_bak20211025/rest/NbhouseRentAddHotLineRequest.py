from app.main.stores.jd.api.base import RestApi

class NbhouseRentAddHotLineRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.phoneName = None
			self.workHourStart = None
			self.workHourEnd = None
			self.phoneLanding = None
			self.type = None

		def getapiname(self):
			return 'jingdong.nbhouse.rent.addHotLine'

			





