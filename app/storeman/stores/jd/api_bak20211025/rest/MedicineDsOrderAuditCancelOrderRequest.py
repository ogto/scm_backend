from app.main.stores.jd.api.base import RestApi

class MedicineDsOrderAuditCancelOrderRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.rejectReason = None
			self.cancelOrderId = None
			self.outOfDeptActual = None
			self.rejectType = None
			self.auditType = None
			self.operateMan = None
			self.reqTimestamp = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.auditCancelOrder'

			





