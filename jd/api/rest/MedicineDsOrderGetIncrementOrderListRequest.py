from jd.api.base import RestApi

class MedicineDsOrderGetIncrementOrderListRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.endDate = None
			self.orderId = None
			self.clientIp = None
			self.pageSize = None
			self.orderStatus = None
			self.page = None
			self.storeId = None
			self.startDate = None
			self.agingType = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.getIncrementOrderList'

			





