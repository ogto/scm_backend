from app.main.stores.jd.api.base import RestApi

class EclpDeliveryApiWaybillQueryApiRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.waybillCode = None
			self.orderNo = None
			self.settleType = None
			self.traderCode = None

		def getapiname(self):
			return 'jingdong.eclp.delivery.storeman.WaybillQueryApi'

			





