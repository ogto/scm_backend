from app.main.stores.jd.api.base import RestApi

class AscReceiveListRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.skuId = None
			self.applyTimeBegin = None
			self.applyTimeEnd = None
			self.expressCode = None
			self.timeoutFlag = None
			self.customerPin = None
			self.customerName = None
			self.customerTel = None
			self.dealType = None
			self.customerExpect = None
			self.jdInterveneFlag = None
			self.approveResult = None
			self.approveReasonCid1 = None
			self.orderShopId = None
			self.returnShopId = None
			self.pageNumber = None
			self.pageSize = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.receive.list'

			





