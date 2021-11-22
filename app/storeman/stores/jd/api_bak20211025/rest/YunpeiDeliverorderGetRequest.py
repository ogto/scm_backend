from app.main.stores.jd.api.base import RestApi

class YunpeiDeliverorderGetRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.way_bill_no = None

		def getapiname(self):
			return 'jingdong.yunpei.deliverorder.get'

			





