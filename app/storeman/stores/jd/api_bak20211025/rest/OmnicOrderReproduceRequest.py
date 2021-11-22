from app.main.stores.jd.api.base import RestApi

class OmnicOrderReproduceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.authKey = None
			self.orderId = None
			self.operateTime = None
			self.remark = None
			self.storeId = None
			self.operateName = None

		def getapiname(self):
			return 'jingdong.omnic.order.reproduce'

			





