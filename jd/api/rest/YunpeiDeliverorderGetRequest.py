from jd.api.base import RestApi

class YunpeiDeliverorderGetRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.way_bill_no = None

		def getapiname(self):
			return 'jingdong.yunpei.deliverorder.get'

			





