from jd.api.base import RestApi

class PopTaurusQueryCouponListByConditionRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
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
			return 'jingdong.pop.taurus.queryCouponListByCondition'

			





