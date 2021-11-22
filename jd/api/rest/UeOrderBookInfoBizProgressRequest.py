from jd.api.base import RestApi

class UeOrderBookInfoBizProgressRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bookBy = None
			self.appId = None
			self.orderNo = None
			self.remark = None
			self.bookDate = None
			self.type = None
			self.bookOperateDate = None

		def getapiname(self):
			return 'jingdong.ue.order.bookInfoBizProgress'

			





