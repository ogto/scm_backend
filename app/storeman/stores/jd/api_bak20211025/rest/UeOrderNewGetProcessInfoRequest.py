from app.main.stores.jd.api.base import RestApi

class UeOrderNewGetProcessInfoRequest(RestApi):
		def __init__(self,domain='gw.storeman.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.appid = None
			self.orderNo = None
			self.venderCode = None

		def getapiname(self):
			return 'jingdong.ue.order.new.getProcessInfo'

			





