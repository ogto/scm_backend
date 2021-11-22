from jd.api.base import RestApi

class EdiArcSendRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.vendorName = None
			self.payableAccountId = None
			self.billType = None
			self.billNo = None
			self.poNo = None
			self.respond = None
			self.amount = None
			self.vendorCode = None

		def getapiname(self):
			return 'jingdong.edi.arc.send'

			





