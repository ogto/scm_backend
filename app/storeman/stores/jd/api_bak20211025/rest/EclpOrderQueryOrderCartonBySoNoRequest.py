from app.main.stores.jd.api.base import RestApi

class EclpOrderQueryOrderCartonBySoNoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.soNo = None

		def getapiname(self):
			return 'jingdong.eclp.order.queryOrderCartonBySoNo'

			





