from app.main.stores.jd.api.base import RestApi

class PopOrderNotPayOrderInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.endDate = None
			self.page = None
			self.pageSize = None

		def getapiname(self):
			return 'jingdong.pop.order.notPayOrderInfo'

			





