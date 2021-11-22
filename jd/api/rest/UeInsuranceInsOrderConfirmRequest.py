from jd.api.base import RestApi

class UeInsuranceInsOrderConfirmRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderNos = None
			self.appId = None

		def getapiname(self):
			return 'jingdong.ue.insurance.insOrderConfirm'

			





