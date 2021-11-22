from jd.api.base import RestApi

class UeOrderNewEvaluateRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.beginDate = None
			self.venderCode = None
			self.endDate = None
			self.appid = None
			self.page = None
			self.serviceTypeId = None
			self.orderNos = None

		def getapiname(self):
			return 'jingdong.ue.order.new.evaluate'

			





