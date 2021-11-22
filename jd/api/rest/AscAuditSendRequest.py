from jd.api.base import RestApi

class AscAuditSendRequest(RestApi):
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
			self.returnContactName = None
			self.returnContactTel = None
			self.returnContactMobile = None
			self.returnZipcode = None
			self.returnProvince = None
			self.returnCity = None
			self.returnCounty = None
			self.returnVillage = None
			self.returnDetailAddress = None
			self.returnAddressType = None
			self.applyDetailIdList = None
			self.invoiceNo = None
			self.invoiceType = None
			self.pickPackage = None
			self.pickDetctPaper = None
			self.operateRemark = None
			self.extJsonStr = None

		def getapiname(self):
			return 'jingdong.asc.audit.send'

			





