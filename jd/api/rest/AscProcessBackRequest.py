from jd.api.base import RestApi

class AscProcessBackRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.buId = None
			self.operatePin = None
			self.operateNick = None
			self.operateRemark = None
			self.serviceId = None
			self.orderId = None
			self.sysVersion = None
			self.consigneeName = None
			self.consigneeTel = None
			self.provinceCode = None
			self.cityCode = None
			self.countyCode = None
			self.villageCode = None
			self.detailAddress = None
			self.repairState = None
			self.applyRemark = None
			self.shipWayId = None
			self.shipWayName = None
			self.expressCode = None
			self.partCodes = None
			self.extJsonStr = None
			self.wareNum = None

		def getapiname(self):
			return 'jingdong.asc.process.back'

			





