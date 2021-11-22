from jd.api.base import RestApi

class B2bMidOrderMiddleProviderQueryOrderListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderTier = None
			self.pageIndex = None
			self.pageSize = None
			self.sortType = None
			self.submitOrderTimeFrom = None
			self.submitOrderTimeTo = None
			self.jdOrderState = None
			self.deliverState = None

		def getapiname(self):
			return 'jingdong.b2b.mid.OrderMiddleProvider.queryOrderList'

			





