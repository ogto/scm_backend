from app.main.stores.jd.api.base import RestApi

class OmnichannelOrderReproduceRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.storeId = None
			self.remark = None
			self.operateName = None
			self.operateTime = None

		def getapiname(self):
			return 'jingdong.omnichannel.order.reproduce'

			





