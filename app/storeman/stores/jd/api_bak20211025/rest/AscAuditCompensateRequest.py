from app.main.stores.jd.api.base import RestApi

class AscAuditCompensateRequest(RestApi):
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
			self.approveReasonCid1 = None
			self.approveReasonCid2 = None
			self.deliveryCenterId = None
			self.deliveryCenterName = None
			self.storeId = None
			self.customerContactName = None
			self.customerContactTel = None
			self.customerContactMobile = None
			self.customerZipcode = None
			self.customerProvince = None
			self.customerCity = None
			self.customerCounty = None
			self.customerVillage = None
			self.customerDetailAddress = None
			self.skuId = None
			self.wareName = None
			self.warePrice = None
			self.wareNum = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.audit.compensate'

			





