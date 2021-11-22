from jd.api.base import RestApi

class AscDoorPickWareListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None

		def getapiname(self):
			return 'jingdong.asc.doorPickWare.list'

			





