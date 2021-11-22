from jd.api.base import RestApi

class AscAuditHomepickRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
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
			self.appendPickware = None
			self.pickupContactName = None
			self.pickupContactTel = None
			self.pickupContactMobile = None
			self.pickupZipcode = None
			self.pickupProvince = None
			self.pickupCity = None
			self.pickupCounty = None
			self.pickupVillage = None
			self.pickupDetailAddress = None
			self.returnContactName = None
			self.returnContactTel = None
			self.returnContactMobile = None
			self.returnZipcode = None
			self.returnProvince = None
			self.returnCity = None
			self.returnCounty = None
			self.returnVillage = None
			self.returnDetailAddress = None
			self.applyDetailIdList = None
			self.invoiceNo = None
			self.invoiceType = None
			self.pickPackage = None
			self.pickDetctPaper = None
			self.returnAddressType = None
			self.pickupStandard = None
			self.operateRemark = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.audit.homepick'

			





