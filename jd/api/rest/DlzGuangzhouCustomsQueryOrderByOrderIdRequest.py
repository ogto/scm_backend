from jd.api.base import RestApi

class DlzGuangzhouCustomsQueryOrderByOrderIdRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.platformId = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.dlz.guangzhou.customs.queryOrderByOrderId'

			





