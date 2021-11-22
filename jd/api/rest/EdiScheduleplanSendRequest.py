from jd.api.base import RestApi

class EdiScheduleplanSendRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.schedulePlanCode = None
			self.jdSku = None
			self.vendorProductId = None
			self.schedulePlanTime = None
			self.quantity = None

		def getapiname(self):
			return 'jingdong.edi.scheduleplan.send'

			





