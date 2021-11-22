from app.main.stores.jd.api.base import RestApi

class YunpeiReturnOrderConfirmRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appKey = None
			self.return_bill_sn = None

		def getapiname(self):
			return 'jingdong.yunpei.returnOrder.confirm'

			





