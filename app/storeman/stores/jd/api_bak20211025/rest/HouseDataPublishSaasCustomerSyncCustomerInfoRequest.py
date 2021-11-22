from app.main.stores.jd.api.base import RestApi

class HouseDataPublishSaasCustomerSyncCustomerInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.tradeAmt = None
			self.city = None
			self.bookAmt = None
			self.project = None
			self.tradeNums = None
			self.uuid = None
			self.customerName = None
			self.attribute1 = None
			self.venderName = None
			self.customerPhone = None
			self.recordTime = None
			self.brokerPhone = None
			self.attribute2 = None
			self.brokerName = None
			self.attribute3 = None
			self.commisionAmt = None
			self.status = None

		def getapiname(self):
			return 'jingdong.house.data.publish.saas.customer.syncCustomerInfo'

			





