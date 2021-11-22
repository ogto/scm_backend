from jd.api.base import RestApi

class YunpeiPurchaseLogisticstrackQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_sn = None

		def getapiname(self):
			return 'jingdong.yunpei.purchase.logisticstrack.query'

			





