from jd.api.base import RestApi

class OrderStatUpLocationGPSRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.nowGPSY = None
			self.nowGPSX = None
			self.orderNo = None
			self.enginnerId = None

		def getapiname(self):
			return 'jingdong.OrderStat.upLocationGPS'

			





