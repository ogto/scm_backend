from jd.api.base import RestApi

class PurchaseOrderSelectInfosRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startDate = None
			self.endDate = None
			self.orderStates = None
			self.pageNo = None
			self.pageSize = None
			self.updateBeginTime = None
			self.updateEndTime = None
			self.provinceId = None
			self.cityId = None
			self.countyId = None
			self.townId = None

		def getapiname(self):
			return 'jingdong.purchase.order.select.infos'

			





