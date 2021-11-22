from app.main.stores.jd.api.base import RestApi

class B2bOrderListGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.req = None

		def getapiname(self):
			return 'jingdong.b2b.order.list.get'

			
	

class SpecSearchInfoReq(object):
		def __init__(self):
			"""
			"""
			self.companyName = None
			self.venderShopName = None


class Req(object):
		def __init__(self):
			"""
			"""
			self.pageIndex = None
			self.pageSize = None
			self.orderTier = None
			self.sortType = None
			self.submitOrderTimeFrom = None
			self.submitOrderTimeTo = None
			self.jdOrderState = None
			self.deliverState = None
			self.extInfo = None
			self.orderPlatform = None
			self.orderSource = None
			self.specSearchInfoReq = None





