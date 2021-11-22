from jd.api.base import RestApi

class EdiVaSendRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorName = None
			self.billNo = None
			self.businessType = None
			self.totalAmount = None
			self.vendorCode = None
			self.settleNo = None
			self.payableAccountId = None
			self.billType = None
			self.verificationBillNo = None
			self.billDate = None
			self.poNo = None
			self.soNo = None
			self.amount = None
			self.memo = None
			self.invoiceNo = None
			self.invoiceCode = None
			self.taxAmount = None

		def getapiname(self):
			return 'jingdong.edi.va.send'

			





