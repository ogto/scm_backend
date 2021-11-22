from app.main.stores.jd.api.base import RestApi

class AscCommonCancelRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.approveNotes = None
			self.sysVersion = None
			self.operateRemark = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.common.cancel'

			





