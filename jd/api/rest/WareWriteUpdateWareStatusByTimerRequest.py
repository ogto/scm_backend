from jd.api.base import RestApi

class WareWriteUpdateWareStatusByTimerRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wareId = None
			self.upTime = None
			self.downTime = None

		def getapiname(self):
			return 'jingdong.ware.write.updateWareStatusByTimer'

			





