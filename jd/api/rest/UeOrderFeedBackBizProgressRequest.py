from jd.api.base import RestApi

class UeOrderFeedBackBizProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operateDate = None
			self.appId = None
			self.orderNo = None
			self.dealRemark = None
			self.type = None
			self.createBy = None
			self.arriveException = None

		def getapiname(self):
			return 'jingdong.ue.order.feedBackBizProgress'

			





