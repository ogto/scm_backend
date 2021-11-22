from app.main.stores.jd.api.base import RestApi

class PopTaurusQueryRefundBillChargeListByConditionRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.businessBeginTime = None
			self.dateType = None
			self.endDate = None
			self.settlementStatus = None
			self.orderId = None
			self.businessEndTime = None
			self.startDate = None

		def getapiname(self):
			return 'jingdong.pop.taurus.queryRefundBillChargeListByCondition'

			





