from app.main.stores.jd.api.base import RestApi

class YunpeiPurchaseOrderCancelRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.order_sn = None

		def getapiname(self):
			return 'jingdong.yunpei.purchase.order.cancel'

			





