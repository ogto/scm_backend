from app.main.stores.jd.api.base import RestApi

class UeOrderQueryCancelOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appId = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.ue.order.queryCancelOrder'

			





