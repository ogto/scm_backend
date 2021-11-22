from app.main.stores.jd.api.base import RestApi

class PopOrderModifyOrderAddrRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.customerName = None
			self.customerPhone = None
			self.provinceId = None
			self.cityId = None
			self.countyId = None
			self.townId = None
			self.detailAddr = None

		def getapiname(self):
			return 'jingdong.pop.order.modifyOrderAddr'

			





