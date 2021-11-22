from app.main.stores.jd.api.base import RestApi

class PopAfsSoaRefundapplyUpdateWarehouseStatusRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.refId = None
			self.status = None

		def getapiname(self):
			return 'jingdong.pop.afs.soa.refundapply.updateWarehouseStatus'

			





