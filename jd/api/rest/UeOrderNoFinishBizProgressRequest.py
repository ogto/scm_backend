from jd.api.base import RestApi

class UeOrderNoFinishBizProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operateDate = None
			self.appId = None
			self.orderNo = None
			self.bookDate = None
			self.reason = None
			self.createBy = None

		def getapiname(self):
			return 'jingdong.ue.order.noFinishBizProgress'

			





