from app.main.stores.jd.api.base import RestApi

class OmnicProduceUpdatestatusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.storeType = None
			self.orderId = None
			self.operateTime = None
			self.storeId = None
			self.operateName = None
			self.status = None
			self.courierId = None
			self.courierName = None
			self.courierPhone = None

		def getapiname(self):
			return 'jingdong.omnic.produce.updatestatus'

			





