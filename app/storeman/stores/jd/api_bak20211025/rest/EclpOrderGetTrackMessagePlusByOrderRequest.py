from app.main.stores.jd.api.base import RestApi

class EclpOrderGetTrackMessagePlusByOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customerCode = None
			self.bizCode = None
			self.type = None

		def getapiname(self):
			return 'jingdong.eclp.order.getTrackMessagePlusByOrder'

			





