from jd.api.base import RestApi

class UeOrderNewFeedBackOrderProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNo = None
			self.operater = None
			self.venderCode = None
			self.appId = None
			self.operateType = None
			self.dealRemark = None
			self.settleCode = None

		def getapiname(self):
			return 'jingdong.ue.order.new.feedBackOrderProgress'

			





