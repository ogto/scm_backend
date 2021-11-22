from app.main.stores.jd.api.base import RestApi

class TempCompleteProviderFindTempCompletePageRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.afsServiceId = None
			self.buId = None
			self.orderId = None
			self.afsApplyTimeBegin = None
			self.afsApplyTimeEnd = None
			self.afsServiceProcessResult = None
			self.waybill = None
			self.customerPin = None
			self.orderType = None
			self.messageStatus = None
			self.searchType = None
			self.operatorPin = None
			self.operatorNick = None
			self.operatorRemark = None
			self.operatorDate = None
			self.platformSrc = None
			self.afsCategoryIdPop = None
			self.verificationCode = None
			self.pageSize = None
			self.pageIndex = None

		def getapiname(self):
			return 'jingdong.TempCompleteProvider.findTempCompletePage'

			





