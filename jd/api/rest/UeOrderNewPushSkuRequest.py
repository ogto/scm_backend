from jd.api.base import RestApi

class UeOrderNewPushSkuRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.stat = None
			self.createBy = None
			self.venderCode = None
			self.appid = None
			self.sku = None

		def getapiname(self):
			return 'jingdong.ue.order.new.pushSku'

			





