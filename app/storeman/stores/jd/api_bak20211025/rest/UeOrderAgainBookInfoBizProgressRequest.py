from app.main.stores.jd.api.base import RestApi

class UeOrderAgainBookInfoBizProgressRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.operateDate = None
			self.orderNo = None
			self.appId = None
			self.bookDate = None
			self.createBy = None

		def getapiname(self):
			return 'jingdong.ue.order.againBookInfoBizProgress'

			





