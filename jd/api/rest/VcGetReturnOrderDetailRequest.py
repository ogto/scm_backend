from jd.api.base import RestApi

class VcGetReturnOrderDetailRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.returnId = None

		def getapiname(self):
			return 'jingdong.vc.get.return.order.detail'

			





