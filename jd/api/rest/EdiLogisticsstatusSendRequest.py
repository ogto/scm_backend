from jd.api.base import RestApi

class EdiLogisticsstatusSendRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorName = None
			self.vendorCode = None
			self.orderType = None
			self.asnCode = None
			self.purchaseOrderCode = None
			self.supposedArrivedDate = None
			self.eventCode = None
			self.eventTime = None
			self.eventLocation = None
			self.eventNameCn = None
			self.eventNameEn = None
			self.nextEventCode = None
			self.nextEventTime = None
			self.nextEventLocation = None
			self.nextEventNameCn = None
			self.nextEventNameEn = None

		def getapiname(self):
			return 'jingdong.edi.logisticsstatus.send'

			





