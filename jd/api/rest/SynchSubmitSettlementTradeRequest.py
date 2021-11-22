from jd.api.base import RestApi

class SynchSubmitSettlementTradeRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.billingBusinessType = None
			self.systemId = None
			self.settleEntityType = None
			self.accountType = None
			self.extJson = None
			self.feeType = None
			self.tradeBillId = None
			self.billingBusinessId = None
			self.accountId = None
			self.createby = None
			self.settleEntityId = None
			self.balance = None
			self.requestId = None
			self.tradeBillType = None
			self.currency = None
			self.direction = None

		def getapiname(self):
			return 'jingdong.synchSubmitSettlementTrade'

			





