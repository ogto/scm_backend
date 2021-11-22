from jd.api.base import RestApi

class AscProcessRenewRequest(RestApi):
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
			self.provinceCode = None
			self.cityCode = None
			self.countyCode = None
			self.villageCode = None
			self.detailAddress = None
			self.consigneeTel = None
			self.applyDescription = None
			self.deliveryCenterId = None
			self.deliveryCenterName = None
			self.storeId = None
			self.collectFreightFlag = None
			self.freightAmount = None
			self.skuId = None
			self.wareName = None
			self.wareNum = None
			self.relationSkuId = None
			self.relationWareType = None
			self.extJsonStr = None
			self.open_id_seller = None
			self.xid_seller = None

		def getapiname(self):
			return 'jingdong.asc.process.renew'

			





