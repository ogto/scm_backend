from app.main.stores.jd.api.base import RestApi

class OpenOmbJosModifyRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorCode = None
			self.weight = None
			self.receiveTownName = None
			self.receiveCityName = None
			self.operateTime = None
			self.receiveTel = None
			self.receiveMobile = None
			self.receiveCountyName = None
			self.receiveProvinceId = None
			self.receiveTownId = None
			self.operateUser = None
			self.waybillCode = None
			self.deptNo = None
			self.orderNo = None
			self.volume = None
			self.receiveName = None
			self.receiveProvinceName = None
			self.senderStation = None
			self.deliverStation = None
			self.receiveAddress = None
			self.receiveCityId = None
			self.receiveCountyId = None

		def getapiname(self):
			return 'jingdong.open.omb.jos.modify'

			





