from jd.api.base import RestApi

class AscFreightSaveRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.serviceId = None
			self.orderId = None
			self.expressCode = None
			self.expressCompany = None
			self.freightMoney = None
			self.shipWayId = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.freight.save'

			





