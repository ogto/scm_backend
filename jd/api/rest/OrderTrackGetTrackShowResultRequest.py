from jd.api.base import RestApi

class OrderTrackGetTrackShowResultRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.userPin = None
			self.orderId = None
			self.userIP = None

		def getapiname(self):
			return 'jingdong.order.track.getTrackShowResult'

			





