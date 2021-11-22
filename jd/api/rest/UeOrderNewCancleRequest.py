from jd.api.base import RestApi

class UeOrderNewCancleRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.venderCode = None
			self.cancleReason = None
			self.appid = None
			self.cancleType = None

		def getapiname(self):
			return 'jingdong.ue.order.new.cancle'

			





