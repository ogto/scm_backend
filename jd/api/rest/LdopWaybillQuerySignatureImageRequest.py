from jd.api.base import RestApi

class LdopWaybillQuerySignatureImageRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.deliveryId = None
			self.customerCode = None

		def getapiname(self):
			return 'jingdong.ldop.waybill.querySignatureImage'

			





