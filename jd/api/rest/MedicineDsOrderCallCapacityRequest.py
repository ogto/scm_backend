from jd.api.base import RestApi

class MedicineDsOrderCallCapacityRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.operateMan = None
			self.reqTimestamp = None
			self.type = None

		def getapiname(self):
			return 'jingdong.medicine.ds.order.callCapacity'

			





